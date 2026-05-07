import { Frank3DViewer } from './viewer3d.js?v=1.0.3';
import { initTabs, switchTab, setBadge } from './tabs.js?v=1.0.3';
import { initMaterials, getSelectedMaterialIds, removeSelection, getMaterialById, allMaterials, createMaterial, reloadMaterials, setRelevantMaterials } from './materials.js?v=1.0.3';
import { MTLParser } from './mtl-parser.js?v=1.0.3';

document.addEventListener('DOMContentLoaded', () => {
    const dropzone = document.getElementById('dropzone');
    const fileInput = document.getElementById('file-input');
    const fileInfo = document.getElementById('file-info');
    const filenameLabel = document.getElementById('filename');
    const filesizeLabel = document.getElementById('filesize');
    const btnRender = document.getElementById('btn-render');
    const jobsList = document.getElementById('jobs-list');
    const gallery = document.getElementById('results-gallery');

    let selectedFile = null;
    let activeJobs = new Set();
    let viewer = null;
    let useCustomCamera = false;

    // ─── Init Tabs ──────────────────────────────────────────────
    initTabs();

    // ─── Init Materials ─────────────────────────────────────────
    initMaterials(onMaterialSelectionChange);

    // "Go to materials" link in render tab
    document.getElementById('go-to-materials')?.addEventListener('click', (e) => {
        e.preventDefault();
        switchTab('materials');
    });

    // ─── Drag and Drop ──────────────────────────────────────────
    dropzone.addEventListener('click', () => fileInput.click());
    dropzone.addEventListener('dragover', (e) => { e.preventDefault(); dropzone.classList.add('active'); });
    dropzone.addEventListener('dragleave', () => dropzone.classList.remove('active'));
    dropzone.addEventListener('drop', async (e) => { 
        e.preventDefault(); 
        dropzone.classList.remove('active'); 
        
        if (e.dataTransfer.items) {
            const items = Array.from(e.dataTransfer.items);
            
            async function readEntry(entry) {
                if (entry.isFile) {
                    return new Promise(resolve => entry.file(f => resolve(f)));
                } else if (entry.isDirectory) {
                    const dirReader = entry.createReader();
                    return new Promise(resolve => {
                        dirReader.readEntries(async (entries) => {
                            const results = await Promise.all(entries.map(readEntry));
                            resolve(results.flat());
                        });
                    });
                }
            }
            
            const promises = [];
            for (let i = 0; i < items.length; i++) {
                const item = items[i];
                if (item.kind === 'file') {
                    const entry = item.webkitGetAsEntry();
                    if (entry) {
                        promises.push(readEntry(entry));
                    }
                }
            }
            
            const allFiles = (await Promise.all(promises)).flat().filter(f => f);
            if (allFiles.length > 0) handleFiles(allFiles);
        } else {
            handleFiles(e.dataTransfer.files); 
        }
    });
    fileInput.addEventListener('change', (e) => handleFiles(e.target.files));

    let selectedFiles = []; // All uploaded files (textures, mtl, etc)
    let mtlMaterials = [];

    function handleFiles(files) {
        if (files.length === 0) return;
        
        const newFiles = Array.from(files);
        
        // Add to pool, replacing duplicates by name
        newFiles.forEach(nf => {
            const index = selectedFiles.findIndex(f => f.name === nf.name);
            if (index > -1) selectedFiles[index] = nf;
            else selectedFiles.push(nf);
        });
        
        // Find the main 3D model file
        const modelExtensions = ['glb', 'gltf', 'obj', 'dae', 'skp', 'fbx'];
        const modelFile = selectedFiles.find(f => {
            const ext = f.name.split('.').pop().toLowerCase();
            return modelExtensions.includes(ext);
        });

        if (!modelFile) {
            alert('Nenhum arquivo de modelo 3D suportado encontrado!');
            return;
        }

        selectedFile = modelFile;
        filenameLabel.textContent = `${modelFile.name} (+${selectedFiles.length - 1} arquivos no pool)`;
        filesizeLabel.textContent = `${(modelFile.size / (1024 * 1024)).toFixed(2)} MB`;
        fileInfo.style.display = 'block';
        btnRender.disabled = false;
        dropzone.style.borderColor = 'var(--success)';
        dropzone.querySelector('p').innerHTML = `Pronto: <strong>${modelFile.name}</strong><br><small style="color:var(--text-dim)">${selectedFiles.length} arquivos prontos para match</small>`;

        checkMtlSuggestions();
        load3DPreview(modelFile);

        // Auto-parse MTL if present in the pool
        const mtlFile = selectedFiles.find(f => f.name.toLowerCase().endsWith('.mtl'));
        if (mtlFile) {
            console.log('[Frank] Auto-parsing detected MTL:', mtlFile.name);
            const reader = new FileReader();
            reader.onload = (e) => {
                mtlMaterials = MTLParser.parse(e.target.result);
                checkMtlSuggestions();
            };
            reader.readAsText(mtlFile);
        }
    }

    // ─── MTL Import Button ───────────────────────────────────────
    const btnOpenMtl = document.getElementById('btn-open-mtl');
    const mtlFileInput = document.getElementById('mtl-file-input');

    if (btnOpenMtl && mtlFileInput) {
        btnOpenMtl.addEventListener('click', () => mtlFileInput.click());
        
        mtlFileInput.addEventListener('change', (e) => {
            const file = e.target.files[0];
            if (!file) return;

            const reader = new FileReader();
            reader.onload = (event) => {
                mtlMaterials = MTLParser.parse(event.target.result);
                console.log('Materials imported from MTL:', mtlMaterials);
                checkMtlSuggestions();
                
                // Re-run auto-match for current parts
                if (viewer) {
                    const structure = viewer.getModelStructure();
                    renderModelStructure(structure);
                }
            };
            reader.readAsText(file);
        });
    }

    function checkMtlSuggestions() {
        const suggestionPanel = document.getElementById('mapping-suggestions');
        if (!viewer) return hideMtlSuggestions();
        
        const structure = viewer.getModelStructure();
        if (!structure || !structure.length) return hideMtlSuggestions();

        const usedMaterialNames = new Set(structure.map(p => (p.materialName || '').toLowerCase()));
        
        const newMaterials = mtlMaterials.filter(mtlMat => 
            usedMaterialNames.has(mtlMat.name.toLowerCase()) &&
            !allMaterials.some(m => m.name.toLowerCase() === mtlMat.name.toLowerCase())
        );

        if (newMaterials.length > 0) {
            // Count missing textures
            let totalMaps = 0;
            let matchedMaps = 0;
            newMaterials.forEach(m => {
                if (m.maps) {
                    Object.values(m.maps).forEach(filename => {
                        totalMaps++;
                        const basename = filename.split(/[/\\]/).pop().toLowerCase();
                        if (selectedFiles.some(f => f.name.toLowerCase() === basename)) matchedMaps++;
                    });
                }
            });

            suggestionPanel.innerHTML = `
                <div class="suggestion-text">
                    📦 <strong>${newMaterials.length}</strong> novos materiais detectados.<br>
                    <small style="color:${matchedMaps === totalMaps ? 'var(--success)' : 'var(--accent)'}">
                        ${matchedMaps}/${totalMaps} texturas encontradas no pool.
                    </small>
                </div>
                <div class="suggestion-actions" style="display:flex; gap:0.5rem; align-items:center;">
                    <input type="text" id="mtl-import-tag" placeholder="Tag (ex: Casa01)" class="search-input" style="width:120px; font-size:0.7rem; padding:4px;">
                    <button class="btn-suggestion" id="btn-import-mtl" style="padding:4px 8px;">Importar Selecionados</button>
                </div>
            `;
            suggestionPanel.style.display = 'flex';
            
            document.getElementById('btn-import-mtl').addEventListener('click', async () => {
                const btn = document.getElementById('btn-import-mtl');
                const tagInput = document.getElementById('mtl-import-tag');
                const tag = tagInput.value.trim();
                const tags = tag ? [tag] : [];

                btn.disabled = true;
                btn.textContent = 'Importando...';
                
                for (const mtlMat of newMaterials) {
                    const pbrProps = {
                        base_color: mtlMat.diffuse || [0.7, 0.7, 0.7, 1],
                        metallic: 0,
                        roughness: 0.5
                    };

                    if (mtlMat.maps) {
                        for (const [key, filename] of Object.entries(mtlMat.maps)) {
                            const basename = filename.split(/[/\\]/).pop().toLowerCase();
                            const matchingFile = selectedFiles.find(f => f.name.toLowerCase() === basename);
                            if (matchingFile) {
                                const formData = new FormData();
                                formData.append('file', matchingFile);
                                try {
                                    const res = await fetch('/materials/upload-texture', { method: 'POST', body: formData });
                                    if (res.ok) {
                                        const data = await res.json();
                                        pbrProps[key] = data.filename;
                                    }
                                } catch (err) { console.error(err); }
                            }
                        }
                    }

                    await createMaterial({
                        material_id: mtlMat.name.toLowerCase().replace(/[^a-z0-9]/g, '_') + '_' + (tag || 'mtl'),
                        name: mtlMat.name,
                        category: 'other',
                        tags: tags,
                        pbr_properties: pbrProps
                    });
                }
                
                alert(`${newMaterials.length} materiais importados com sucesso!`);
                await reloadMaterials();
                
                if (viewer) {
                    const freshStructure = viewer.getModelStructure();
                    renderModelStructure(freshStructure);
                }

                hideMtlSuggestions();
                btn.disabled = false;
                btn.textContent = 'Importar Selecionados';
            });
        } else {
            hideMtlSuggestions();
        }
    }

    function hideMtlSuggestions() {
        const suggestionPanel = document.getElementById('mapping-suggestions');
        if (suggestionPanel) suggestionPanel.style.display = 'none';
    }

    // ─── 3D Preview ─────────────────────────────────────────────
    async function load3DPreview(file) {
        const section = document.getElementById('viewer-section');
        const loading = document.getElementById('viewer-loading');
        const ext = file.name.split('.').pop().toLowerCase();
        
        section.style.display = 'block';
        loading.style.display = 'flex';
        loading.innerHTML = '<div class="spinner"></div><p>Carregando preview...</p>';
        section.classList.add('fade-in');
        
        if (viewer) { viewer.dispose(); viewer = null; }
        
        try {
            viewer = new Frank3DViewer('viewer-container');
            viewer.onCameraChange = (p) => { updateCameraInfo(p); enableCustomCamera(p); };

            if (ext === 'skp') {
                loading.innerHTML = '<div class="spinner"></div><p>Convertendo SketchUp para preview (aguarde)...</p>';
                const formData = new FormData();
                formData.append('file', file);
                const res = await fetch('/render/preview', { method: 'POST', body: formData });
                if (!res.ok) throw new Error('Falha na conversão para preview');
                const blob = await res.blob();
                const previewFile = new File([blob], 'preview.glb', { type: 'model/gltf-binary' });
                await viewer.loadFromFile(previewFile);
            } else {
                await viewer.loadFromFile(file);
            }

            loading.style.display = 'none';
            const p = viewer.getCameraParams();
            updateCameraInfo(p);
            enableCustomCamera(p);

            // Extract and show model structure
            const structure = viewer.getModelStructure();
            renderModelStructure(structure);
            checkMtlSuggestions();
        } catch (err) {
            loading.innerHTML = `<p style="color:var(--error);">⚠️ Falha ao carregar preview</p><p style="font-size:0.8rem;color:var(--text-dim);margin-top:0.5rem;">${err.message||''}</p>`;
        }
    }

    function renderModelStructure(structure) {
        const section = document.getElementById('model-structure-section');
        const list = document.getElementById('model-parts-list');
        const countBadge = document.getElementById('part-count');

        if (!structure || structure.length === 0) {
            section.style.display = 'none';
            return;
        }

        section.style.display = 'block';
        const partBadge = document.getElementById('v-part-badge');
        if (partBadge) {
            partBadge.textContent = structure.length;
            partBadge.style.display = structure.length > 0 ? 'inline-block' : 'none';
        }
        list.innerHTML = '';

        // Collect names for catalog sorting
        const relevantNames = [];
        structure.forEach(p => {
            if (p.name) relevantNames.push(p.name);
            if (p.materialName) relevantNames.push(p.materialName);
        });
        setRelevantMaterials(relevantNames);

        structure.forEach(part => {
            const row = document.createElement('div');
            row.className = 'model-part-row';
            
            // Auto-match logic
            // Auto-match logic
            let selectedMatId = '';
            let match = null;
            if (part.materialName) {
                match = allMaterials.find(m => 
                    m.name.toLowerCase() === part.materialName.toLowerCase() ||
                    m.material_id.toLowerCase() === part.materialName.toLowerCase().replace(/[^a-z0-9]/g, '_')
                );
                if (match) {
                    console.log(`[Frank] Auto-matched part '${part.name}' (mat: ${part.materialName}) -> ${match.material_id}`);
                    selectedMatId = match.material_id;
                    if (viewer) {
                        viewer.setPartMaterial(part.name, match.pbr_properties);
                    }
                } else {
                    console.log(`[Frank] No match found for part '${part.name}' (mat: ${part.materialName})`);
                }
            }

            row.innerHTML = `
                <span class="part-type-icon">${part.type === 'mesh' ? '📦' : '📁'}</span>
                <span class="part-name" title="${part.name}">${part.name}</span>
                <div class="part-swatch" id="swatch-${part.name}" style="background-color: ${selectedMatId ? 'var(--success)' : 'transparent'}"></div>
                <select class="part-material-select" data-part="${part.name}">
                    <option value="">Padrão do Modelo</option>
                    ${allMaterials.map(m => `<option value="${m.material_id}" ${m.material_id === selectedMatId ? 'selected' : ''}>${m.name}</option>`).join('')}
                </select>
            `;

            const select = row.querySelector('select');
            
            // Highlight in viewer on hover
            row.addEventListener('mouseenter', () => {
                if (viewer) viewer.highlightPart(part.name);
                row.style.borderColor = 'var(--accent)';
                row.style.background = 'rgba(52, 152, 219, 0.1)';
            });
            
            row.addEventListener('mouseleave', () => {
                if (viewer) viewer.clearHighlight();
                row.style.borderColor = 'var(--border)';
                row.style.background = 'rgba(255, 255, 255, 0.03)';
            });

            select.addEventListener('change', (e) => {
                const mid = e.target.value;
                const swatch = row.querySelector('.part-swatch');
                if (mid) {
                    const m = allMaterials.find(x => x.material_id === mid);
                    const bc = m.pbr_properties?.base_color || [0.5,0.5,0.5,1];
                    swatch.style.background = `rgb(${Math.round(bc[0]*255)},${Math.round(bc[1]*255)},${Math.round(bc[2]*255)})`;
                    swatch.style.borderColor = 'var(--accent)';
                    row.classList.add('mapped');
                } else {
                    swatch.style.background = 'transparent';
                    swatch.style.borderColor = 'var(--border)';
                    row.classList.remove('mapped');
                }
            });

            // --- Auto-Match Logic ---
            // 0. Try to match by the material name assigned in the 3D model (e.g. from usemtl in OBJ)
            let matchedMaterial = null;
            if (part.materialName) {
                matchedMaterial = allMaterials.find(m => 
                    m.name.toLowerCase() === part.materialName.toLowerCase() ||
                    m.sketchup_material_name?.toLowerCase() === part.materialName.toLowerCase()
                );
            }

            // 1. Try to match by mesh name exactly
            if (!matchedMaterial) {
                matchedMaterial = allMaterials.find(m => 
                    m.name.toLowerCase() === part.name.toLowerCase() ||
                    part.name.toLowerCase().includes(m.name.toLowerCase())
                );
            }

            // If not matched by name, check if mesh name matches an MTL entry, 
            // and if that MTL entry matches a catalog material
            if (!matchedMaterial && mtlMaterials.length > 0) {
                const mtlMatch = mtlMaterials.find(m => part.name.toLowerCase().includes(m.name.toLowerCase()));
                if (mtlMatch) {
                    matchedMaterial = allMaterials.find(mat => mat.name.toLowerCase() === mtlMatch.name.toLowerCase());
                }
            }

            if (matchedMaterial) {
                select.value = matchedMaterial.material_id;
                select.dispatchEvent(new Event('change'));
                row.style.borderLeft = '4px solid var(--success)';
            }

            list.appendChild(row);
        });
    }

    function hideModelStructure() {
        document.getElementById('model-structure-section').style.display = 'none';
    }

    function hide3DPreview() {
        document.getElementById('viewer-section').style.display = 'none';
        useCustomCamera = false;
        const sel = document.getElementById('camera');
        document.getElementById('camera-custom-option').style.display = 'none';
        sel.value = 'auto';
        if (viewer) { viewer.dispose(); viewer = null; }
        setRelevantMaterials([]);
    }

    function updateCameraInfo(p) {
        // Update input values (only if not currently focused to avoid jumpy typing)
        const inputs = [
            ['cam-pos-x', p.position.x], ['cam-pos-y', p.position.y], ['cam-pos-z', p.position.z],
            ['cam-target-x', p.target.x], ['cam-target-y', p.target.y], ['cam-target-z', p.target.z]
        ];
        
        inputs.forEach(([id, val]) => {
            const el = document.getElementById(id);
            if (el && document.activeElement !== el) {
                el.value = val.toFixed(1);
            }
        });

        document.getElementById('fov-value').textContent = `${Math.round(p.fov)}°`;
        document.getElementById('fov-slider').value = p.fov;
    }

    // Sync inputs back to viewer
    function syncInputsToViewer() {
        if (!viewer) return;
        const px = document.getElementById('cam-pos-x'), py = document.getElementById('cam-pos-y'), pz = document.getElementById('cam-pos-z');
        const tx = document.getElementById('cam-target-x'), ty = document.getElementById('cam-target-y'), tz = document.getElementById('cam-target-z');
        
        if (!px || !tx) return;

        viewer.setCameraParams({
            position: {
                x: parseFloat(px.value) || 0,
                y: parseFloat(py.value) || 0,
                z: parseFloat(pz.value) || 0
            },
            target: {
                x: parseFloat(tx.value) || 0,
                y: parseFloat(ty.value) || 0,
                z: parseFloat(tz.value) || 0
            }
        });
    }

    document.querySelectorAll('.coord-input').forEach(el => {
        el.addEventListener('change', syncInputsToViewer);
    });

    document.getElementById('check-precision')?.addEventListener('change', (e) => {
        if (viewer) {
            viewer.setControlSpeed(e.target.checked ? 0.2 : 1.0);
        }
    });

    document.querySelectorAll('.nudge-btns button').forEach(btn => {
        btn.addEventListener('click', () => {
            const input = document.getElementById(btn.dataset.id);
            const dir = parseInt(btn.dataset.dir);
            const step = parseFloat(input.step) || 1.0;
            const current = parseFloat(input.value) || 0;
            input.value = (current + (dir * step)).toFixed(1);
            syncInputsToViewer();
        });
    });

    function enableCustomCamera(p) {
        useCustomCamera = true;
        document.getElementById('camera-position').value = JSON.stringify(p.blender.position);
        document.getElementById('camera-target').value = JSON.stringify(p.blender.target);
        document.getElementById('camera-fov').value = p.blender.fov;
        document.getElementById('camera-custom-option').style.display = 'block';
        document.getElementById('camera').value = 'custom';
    }

    // Viewer toolbar
    document.querySelectorAll('.preset-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            if (!viewer) return;
            viewer.setCameraPreset(btn.dataset.preset, true);
            document.querySelectorAll('.preset-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
        });
    });
    document.getElementById('btn-reset-camera').addEventListener('click', () => {
        if (viewer) { viewer.resetCamera(); document.querySelectorAll('.preset-btn').forEach(b => b.classList.remove('active')); document.querySelector('[data-preset="perspective"]').classList.add('active'); }
    });
    document.getElementById('fov-slider').addEventListener('input', (e) => {
        if (viewer) { viewer.setFOV(parseFloat(e.target.value)); document.getElementById('fov-value').textContent = `${e.target.value}°`; }
    });
    document.getElementById('camera').addEventListener('change', (e) => {
        if (e.target.value !== 'custom') { useCustomCamera = false; document.getElementById('camera-position').value = ''; document.getElementById('camera-target').value = ''; document.getElementById('camera-fov').value = ''; }
    });

    // ─── Health & Init ──────────────────────────────────────────
    function onMaterialSelectionChange(ids) {
        const section = document.getElementById('selected-materials-section');
        const chips = document.getElementById('selected-materials-chips');
        setBadge('materials-badge', ids.length);

        if (ids.length === 0) {
            section.style.display = 'none';
            return;
        }
        section.style.display = 'block';
        chips.innerHTML = '';
        ids.forEach(id => {
            const m = getMaterialById(id);
            if (!m) return;
            const bc = m.pbr_properties?.base_color || [0.5,0.5,0.5,1];
            const css = `rgb(${Math.round(bc[0]*255)},${Math.round(bc[1]*255)},${Math.round(bc[2]*255)})`;
            const chip = document.createElement('span');
            chip.className = 'material-chip';
            chip.innerHTML = `<span class="material-chip-swatch" style="background:${css}"></span>${m.name}<button class="material-chip-remove" data-id="${id}">✕</button>`;
            chip.querySelector('.material-chip-remove').addEventListener('click', () => removeSelection(id));
            chips.appendChild(chip);
        });
    }

    // ─── Render Submission ──────────────────────────────────────
    btnRender.addEventListener('click', async () => {
        if (!selectedFile) return;
        const formData = new FormData();
        formData.append('file', selectedFile);
        formData.append('samples', document.getElementById('samples').value);
        formData.append('resolution_x', document.getElementById('res-x').value);
        formData.append('resolution_y', document.getElementById('res-y').value);
        formData.append('device', document.getElementById('device').value);

        if (useCustomCamera) {
            formData.append('camera_angle', 'custom');
            formData.append('camera_position', document.getElementById('camera-position').value);
            formData.append('camera_target', document.getElementById('camera-target').value);
            formData.append('camera_fov', document.getElementById('camera-fov').value);
        } else {
            formData.append('camera_angle', document.getElementById('camera').value);
        }

        // Include MTL file if available
        const mtlInput = document.getElementById('mtl-file-input');
        if (mtlInput && mtlInput.files && mtlInput.files[0]) {
            formData.append('mtl_file', mtlInput.files[0]);
        }

        const matIds = getSelectedMaterialIds();
        const partMappings = {};
        document.querySelectorAll('.part-material-select').forEach(sel => {
            if (sel.value) partMappings[sel.dataset.part] = sel.value;
        });

        if (Object.keys(partMappings).length > 0) {
            formData.append('material_overrides', JSON.stringify(partMappings));
        } else if (matIds.length > 0) {
            formData.append('material_overrides', JSON.stringify(matIds));
        }

        btnRender.disabled = true;
        btnRender.textContent = 'Enviando...';
        try {
            const res = await fetch('/render', { method: 'POST', body: formData });
            if (!res.ok) { const e = await res.json(); throw new Error(e.detail || 'Falha'); }
            const data = await res.json();
            addJobToQueue(data.job_id, selectedFile.name);
            selectedFile = null;
            btnRender.textContent = 'Iniciar Renderização';
            fileInfo.style.display = 'none';
            dropzone.style.borderColor = 'var(--border)';
            dropzone.querySelector('p').innerHTML = 'Arraste seu arquivo <strong>.glb</strong> ou <strong>.gltf</strong> aqui';
            hide3DPreview();
        } catch (error) {
            alert(`Erro: ${error.message}`);
            btnRender.disabled = false;
            btnRender.textContent = 'Iniciar Renderização';
        }
    });

    // ─── Job Queue ──────────────────────────────────────────────
    function addJobToQueue(jobId, filename) {
        if (activeJobs.has(jobId)) return;
        activeJobs.add(jobId);
        setBadge('queue-badge', activeJobs.size);

        const empty = document.getElementById('queue-empty');
        if (empty) empty.style.display = 'none';

        const el = document.createElement('div');
        el.className = 'job-item fade-in';
        el.id = `job-${jobId}`;
        el.innerHTML = `<div class="job-header"><strong>${filename}</strong><span class="job-status status-pending">Pendente</span></div><div class="progress-bar"><div class="progress-fill" style="width:0%"></div></div><p style="font-size:0.7rem;color:var(--text-dim);margin-top:0.5rem">ID: ${jobId}</p>`;
        jobsList.prepend(el);
        pollStatus(jobId);
    }

    async function pollStatus(jobId) {
        const el = document.getElementById(`job-${jobId}`);
        const badge = el.querySelector('.job-status');
        const fill = el.querySelector('.progress-fill');
        const iv = setInterval(async () => {
            try {
                const res = await fetch(`/render/status/${jobId}`);
                const d = await res.json();
                badge.textContent = d.status;
                badge.className = `job-status status-${d.status}`;
                if (d.progress) fill.style.width = `${d.progress}%`;
                if (d.status === 'completed') {
                    clearInterval(iv);
                    fill.style.width = '100%';
                    activeJobs.delete(jobId);
                    setBadge('queue-badge', activeJobs.size);
                    setTimeout(() => { el.remove(); loadGallery(); if (activeJobs.size === 0) { const e = document.getElementById('queue-empty'); if (e) e.style.display = 'block'; } }, 2000);
                } else if (d.status === 'failed') {
                    clearInterval(iv);
                    activeJobs.delete(jobId);
                    setBadge('queue-badge', activeJobs.size);
                }
            } catch (e) { console.error(e); }
        }, 2000);
    }

    // ─── Gallery ────────────────────────────────────────────────
    async function loadGallery() {
        try {
            const res = await fetch('/render/gallery?per_page=50');
            const data = await res.json();
            gallery.innerHTML = '';
            setBadge('gallery-badge', data.total);
            if (data.items.length === 0) {
                gallery.innerHTML = '<div class="gallery-empty"><div class="gallery-empty-icon">🖼️</div><p>Nenhum render concluído.</p><p class="gallery-empty-hint">Envie um modelo 3D para começar.</p></div>';
                return;
            }
            data.items.forEach(item => addGalleryCard(item));
            document.getElementById('gallery-count').textContent = data.total > 0 ? `(${data.total})` : '';
        } catch (e) { console.error(e); }
    }

    function addGalleryCard(item) {
        const card = document.createElement('div');
        card.className = 'render-card fade-in';
        card.id = `gallery-${item.job_id}`;
        const fn = item.original_filename || 'model.glb';
        const date = item.created_at ? formatDate(item.created_at) : '';
        const stars = buildStars(item.rating || 0, item.job_id);
        const shortId = item.job_id.slice(0, 8);
        card.innerHTML = `
            <div class="render-card-image">${item.has_output ? `<img src="/render/download/${item.job_id}" alt="${fn}" loading="lazy">` : '<div class="render-card-placeholder">📷</div>'}</div>
            <div class="render-card-info">
                <div class="render-card-top"><span class="render-card-filename" title="${fn}">${fn}</span><span class="render-card-meta">${date}</span></div>
                <div class="render-card-bottom">
                    <div class="render-card-stars" data-job-id="${item.job_id}">${stars}</div>
                    <div class="render-card-actions">
                        ${item.has_output ? `<a href="/render/download/${item.job_id}" class="render-action-btn" download="render_${shortId}.png" title="Download">↓</a>` : ''}
                        <button class="render-action-btn render-delete-btn" data-job-id="${item.job_id}" title="Excluir">✕</button>
                    </div>
                </div>
            </div>`;
        gallery.appendChild(card);
        card.querySelectorAll('.star-btn').forEach(s => s.addEventListener('click', () => rateRender(item.job_id, parseInt(s.dataset.rating))));
        card.querySelector('.render-delete-btn')?.addEventListener('click', () => deleteRender(item.job_id));
    }

    function buildStars(rating, jobId) {
        let h = '';
        for (let i = 1; i <= 5; i++) h += `<button class="star-btn ${i <= rating ? 'star-filled' : 'star-empty'}" data-rating="${i}">★</button>`;
        return h;
    }

    async function rateRender(jobId, rating) {
        try {
            const res = await fetch(`/render/gallery/${jobId}/rate?rating=${rating}`, { method: 'PATCH' });
            if (res.ok) {
                const c = document.querySelector(`[data-job-id="${jobId}"].render-card-stars`);
                if (c) { c.innerHTML = buildStars(rating, jobId); c.querySelectorAll('.star-btn').forEach(s => s.addEventListener('click', () => rateRender(jobId, parseInt(s.dataset.rating)))); }
            }
        } catch (e) { console.error(e); }
    }

    async function deleteRender(jobId) {
        if (!confirm('Excluir este render?')) return;
        try {
            const res = await fetch(`/render/gallery/${jobId}`, { method: 'DELETE' });
            if (res.ok) { const c = document.getElementById(`gallery-${jobId}`); if (c) { c.style.opacity = '0'; setTimeout(() => { c.remove(); if (!gallery.children.length) loadGallery(); }, 300); } }
        } catch (e) { console.error(e); }
    }

    function formatDate(iso) {
        const d = new Date(iso), now = new Date(), ms = now - d;
        const mins = Math.floor(ms/60000), hrs = Math.floor(ms/3600000), days = Math.floor(ms/86400000);
        if (mins < 1) return 'agora';
        if (mins < 60) return `${mins}min`;
        if (hrs < 24) return `${hrs}h`;
        if (days < 7) return `${days}d`;
        return d.toLocaleDateString('pt-BR');
    }

    document.getElementById('btn-refresh').addEventListener('click', loadGallery);

    // ─── Health & Init ──────────────────────────────────────────
    async function checkStatus() {
        try {
            const res = await fetch('/health');
            const d = await res.json();
            document.getElementById('api-status').textContent = d.status === 'healthy' ? 'Online' : 'Offline';
        } catch (e) {
            document.getElementById('api-status').textContent = 'Offline';
            document.getElementById('api-status').className = 'job-status status-failed';
        }
    }

    checkStatus();
    loadGallery();
});
