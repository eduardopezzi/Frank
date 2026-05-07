/** Materials catalog CRUD + selection manager */

// ─── State ──────────────────────────────────────────────────────
export let allMaterials = [];
let selectedIds = new Set();
let activeCategory = '';

const categoryLabels = {
    concrete: 'Concreto', wood: 'Madeira', glass: 'Vidro',
    metal: 'Metal', wall: 'Parede', floor: 'Piso', stone: 'Pedra'
};

function getCategoryLabel(cat) {
    return categoryLabels[cat] || (cat ? cat.charAt(0).toUpperCase() + cat.slice(1) : 'Outros');
}

// ─── Public API ─────────────────────────────────────────────────

export function getSelectedMaterialIds() {
    return [...selectedIds];
}

export async function initMaterials(onSelectionChange) {
    _onSelectionChange = onSelectionChange;
    await loadMaterials();
    _bindSearch();
    _bindCategories();
    _bindModal();
    _bindNewBtn();
}

export async function reloadMaterials() {
    await loadMaterials();
}

export async function createMaterial(payload) {
    const res = await fetch('/materials', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
    });
    return res;
}

let _onSelectionChange = () => {};

// ─── Load & Render ──────────────────────────────────────────────

async function loadMaterials() {
    try {
        const res = await fetch('/materials');
        allMaterials = await res.json();
        renderGrid(allMaterials);
        renderCategoryButtons();
    } catch (e) { console.error('Failed to load materials:', e); }
}

function renderGrid(materials) {
    const grid = document.getElementById('materials-grid');
    grid.innerHTML = '';
    if (materials.length === 0) {
        grid.innerHTML = '<div class="materials-empty">Nenhum material encontrado.</div>';
        return;
    }
    materials.forEach(m => grid.appendChild(createCard(m)));
}

function createCard(m) {
    const pbr = m.pbr_properties || {};
    const bc = pbr.base_color || [0.5, 0.5, 0.5, 1];
    const cssColor = `rgb(${Math.round(bc[0]*255)},${Math.round(bc[1]*255)},${Math.round(bc[2]*255)})`;
    const selected = selectedIds.has(m.material_id);

    // Image preview or solid color
    const hasTexture = !!pbr.base_color_map;
    const swatchStyle = hasTexture 
        ? `background-image: url('/textures/${pbr.base_color_map}'); background-size: cover; background-position: center;` 
        : `background: ${cssColor};`;

    const card = document.createElement('div');
    card.className = `mat-card${selected ? ' selected' : ''}`;
    card.dataset.id = m.material_id;
    card.innerHTML = `
        <div class="mat-card-check">✓</div>
        <div class="mat-card-swatch" style="${swatchStyle}"></div>
        <div class="mat-card-actions">
            <button class="mat-action-btn edit" title="Editar">✎</button>
            <button class="mat-action-btn delete" title="Excluir">✕</button>
        </div>
        <div class="mat-card-body">
            <div class="mat-card-name">${m.name}</div>
            <div class="mat-card-desc">${m.description || ''}</div>
            <div class="mat-card-tags">
                ${(m.tags || []).map(t => `<span class="mat-tag-pill">${t}</span>`).join('')}
            </div>
            <div class="mat-card-props">
                <span class="mat-prop-tag">${getCategoryLabel(m.category)}</span>
                <span class="mat-prop-tag">M ${Math.round((pbr.metallic||0)*100)}%</span>
                <span class="mat-prop-tag">R ${Math.round((pbr.roughness||0.5)*100)}%</span>
            </div>
        </div>`;

    // Select/deselect on card click
    card.addEventListener('click', (e) => {
        if (e.target.closest('.mat-action-btn')) return;
        toggleSelection(m.material_id);
    });

    // Edit
    card.querySelector('.edit').addEventListener('click', (e) => {
        e.stopPropagation();
        openModal(m);
    });

    // Delete
    card.querySelector('.delete').addEventListener('click', (e) => {
        e.stopPropagation();
        deleteMaterial(m.material_id, m.name);
    });

    return card;
}

// ─── Selection ──────────────────────────────────────────────────

function toggleSelection(id) {
    if (selectedIds.has(id)) selectedIds.delete(id);
    else selectedIds.add(id);
    
    // Update card visuals
    document.querySelectorAll('.mat-card').forEach(c => {
        c.classList.toggle('selected', selectedIds.has(c.dataset.id));
    });
    _onSelectionChange([...selectedIds]);
}

export function removeSelection(id) {
    selectedIds.delete(id);
    document.querySelectorAll('.mat-card').forEach(c => {
        c.classList.toggle('selected', selectedIds.has(c.dataset.id));
    });
    _onSelectionChange([...selectedIds]);
}

// ─── Search & Filter ────────────────────────────────────────────

function _bindSearch() {
    const input = document.getElementById('material-search');
    let debounce;
    input.addEventListener('input', () => {
        clearTimeout(debounce);
        debounce = setTimeout(() => filterMaterials(), 200);
    });
}

function _bindCategories() {
    document.getElementById('material-categories').addEventListener('click', (e) => {
        const btn = e.target.closest('.cat-btn');
        if (!btn) return;
        activeCategory = btn.dataset.category;
        document.querySelectorAll('.cat-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        filterMaterials();
    });
}

function renderCategoryButtons() {
    const container = document.getElementById('material-categories');
    const cats = [...new Set(allMaterials.map(m => m.category))].sort();
    // Keep "Todos" button, add others
    container.innerHTML = '<button class="cat-btn active" data-category="">Todos</button>';
    cats.forEach(c => {
        container.innerHTML += `<button class="cat-btn" data-category="${c}">${getCategoryLabel(c)}</button>`;
    });
}

let relevantNames = [];

export function setRelevantMaterials(names) {
    relevantNames = names.map(n => n.toLowerCase());
    filterMaterials(); // Re-render with new sort
}

function filterMaterials() {
    const query = document.getElementById('material-search').value.toLowerCase();
    let filtered = [...allMaterials]; // Work on a copy
    
    // 1. Filter by category
    if (activeCategory) filtered = filtered.filter(m => m.category === activeCategory);
    
    // 2. Filter by search query
    if (query) {
        filtered = filtered.filter(m =>
            (m.name + ' ' + (m.description||'') + ' ' + (m.tags||[]).join(' ')).toLowerCase().includes(query)
        );
    }
    
    // 3. Sort by relevance (materials in the model first)
    if (relevantNames.length > 0) {
        filtered.sort((a, b) => {
            const aName = a.name.toLowerCase();
            const bName = b.name.toLowerCase();
            const aSkp = (a.sketchup_material_name || '').toLowerCase();
            const bSkp = (b.sketchup_material_name || '').toLowerCase();
            
            const aIsRelevant = relevantNames.includes(aName) || relevantNames.some(rn => aSkp.includes(rn));
            const bIsRelevant = relevantNames.includes(bName) || relevantNames.some(rn => bSkp.includes(rn));
            
            if (aIsRelevant && !bIsRelevant) return -1;
            if (!aIsRelevant && bIsRelevant) return 1;
            return 0; // Maintain original order otherwise
        });
    }
    
    renderGrid(filtered);
}

// ─── Modal (Create / Edit) ──────────────────────────────────────

let editingId = null;
let currentGeneratedMaps = null;

function _bindNewBtn() {
    document.getElementById('btn-new-material').addEventListener('click', () => openModal(null));
}

function _bindModal() {
    _bindPHSearch();
    const overlay = document.getElementById('material-modal');
    const form = document.getElementById('material-form');

    // Close on overlay click
    overlay.addEventListener('click', (e) => { if (e.target === overlay) closeModal(); });

    // PBR range live values
    ['mat-metallic', 'mat-roughness', 'mat-alpha', 'mat-transmission'].forEach(id => {
        const el = document.getElementById(id);
        el.addEventListener('input', () => {
            document.getElementById(id + '-val').textContent = el.value + '%';
        });
    });

    // Smart PBR Generation from Image
    _bindPbrGenerator();

    // Category toggle
    const catSelect = document.getElementById('mat-category');
    const customCatGroup = document.getElementById('mat-category-custom-group');
    catSelect.addEventListener('change', () => {
        customCatGroup.style.display = catSelect.value === 'custom' ? 'block' : 'none';
    });

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        await saveMaterial();
    });
}

function _bindPbrGenerator() {
    const dropzone = document.getElementById('gen-dropzone');
    const fileInput = document.getElementById('gen-file-input');
    const loading = document.getElementById('gen-loading');

    if (!dropzone) return;

    dropzone.addEventListener('click', () => fileInput.click());
    
    // Drag and Drop listeners
    dropzone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropzone.style.borderColor = 'var(--accent)';
        dropzone.style.background = 'rgba(52, 152, 219, 0.1)';
    });

    dropzone.addEventListener('dragleave', () => {
        dropzone.style.borderColor = 'var(--border)';
        dropzone.style.background = 'transparent';
    });

    dropzone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropzone.style.borderColor = 'var(--border)';
        dropzone.style.background = 'transparent';
        
        if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
            handleGenFile(e.dataTransfer.files[0]);
        }
    });
    
    fileInput.addEventListener('change', (e) => {
        if (e.target.files && e.target.files.length > 0) {
            handleGenFile(e.target.files[0]);
        }
    });

    async function handleGenFile(file) {
        if (!file.type.startsWith('image/')) {
            alert('Por favor, envie um arquivo de imagem.');
            return;
        }

        // Show loading
        dropzone.style.display = 'none';
        loading.style.display = 'flex';

        const formData = new FormData();
        formData.append('file', file);

        try {
            const res = await fetch('/materials/generate', {
                method: 'POST',
                body: formData
            });

            if (!res.ok) throw new Error('Falha na geração PBR');

            const data = await res.json();
            console.log('PBR Maps Generated:', data);

            // Populate form
            document.getElementById('mat-name').value = data.name;
            setRange('mat-metallic', (data.pbr_properties.metallic || 0) * 100);
            setRange('mat-roughness', (data.pbr_properties.roughness || 0.5) * 100);
            
            // Store map paths for saveMaterial
            currentGeneratedMaps = data.pbr_properties;
            
            // Visual feedback
            dropzone.innerHTML = `<span>✅ Imagem processada!</span>`;
            
            const resultsDiv = document.getElementById('gen-results');
            if (resultsDiv) {
                resultsDiv.style.display = 'block';
                resultsDiv.innerHTML = `
                    <p style="margin-bottom: 5px; font-weight: bold;">Mapas PBR detectados:</p>
                    <ul style="list-style: none; padding-left: 10px;">
                        <li>✨ Albedo: ${data.pbr_properties.base_color_map}</li>
                        <li>⛰️ Normal: ${data.pbr_properties.normal_map}</li>
                        <li>🌑 Rugosidade: ${data.pbr_properties.roughness_map}</li>
                        <li>📏 Deslocamento: ${data.pbr_properties.displacement_map}</li>
                    </ul>
                `;

                // Update texture preview in modal
                const texPreview = document.getElementById('mat-texture-preview');
                if (texPreview && data.pbr_properties.base_color_map) {
                    texPreview.style.backgroundImage = `url('/textures/${data.pbr_properties.base_color_map}')`;
                    texPreview.style.display = 'block';
                }
            }
        } catch (err) {
            alert('Erro ao gerar PBR: ' + err.message);
        } finally {
            loading.style.display = 'none';
            dropzone.style.display = 'flex';
        }
    }
}

function openModal(material) {
    editingId = material ? material.material_id : null;
    currentGeneratedMaps = null;
    const modal = document.getElementById('material-modal');
    const title = document.getElementById('modal-title');
    const submitBtn = document.getElementById('btn-submit-material');
    const idInput = document.getElementById('mat-id');
    
    // Reset tabs
    if (typeof switchModalTab === 'function') switchModalTab('manual');

    const dropzone = document.getElementById('gen-dropzone');
    if (dropzone) {
        dropzone.style.display = 'flex';
        dropzone.innerHTML = '<span>📸 Arraste ou clique para gerar mapas (Albedo, Normal, etc)</span>';
    }
    const loading = document.getElementById('gen-loading');
    if (loading) loading.style.display = 'none';

    const resultsDiv = document.getElementById('gen-results');
    if (resultsDiv) {
        resultsDiv.style.display = 'none';
        resultsDiv.innerHTML = '';
    }

    title.textContent = material ? 'Editar Material' : 'Novo Material';
    submitBtn.textContent = material ? 'Salvar' : 'Criar Material';
    idInput.disabled = !!material;

    const texPreview = document.getElementById('mat-texture-preview');
    if (material) {
        const pbr = material.pbr_properties || {};
        const bc = pbr.base_color || [0.5,0.5,0.5,1];
        idInput.value = material.material_id;
        document.getElementById('mat-name').value = material.name;
        document.getElementById('mat-category').value = material.category;
        document.getElementById('mat-tags').value = (material.tags || []).join(', ');
        document.getElementById('mat-desc').value = material.description || '';
        document.getElementById('mat-color').value = rgbToHex(bc[0], bc[1], bc[2]);
        
        if (pbr.base_color_map) {
            texPreview.style.backgroundImage = `url('/textures/${pbr.base_color_map}')`;
            texPreview.style.display = 'block';
        } else {
            texPreview.style.display = 'none';
        }

        setRange('mat-metallic', (pbr.metallic||0)*100);
        setRange('mat-roughness', (pbr.roughness||0.5)*100);
        setRange('mat-alpha', (pbr.alpha||1)*100);
        document.getElementById('mat-ior').value = pbr.ior || 1.45;
        setRange('mat-transmission', (pbr.transmission||0)*100);
    } else {
        document.getElementById('material-form').reset();
        document.getElementById('mat-color').value = '#888888';
        texPreview.style.display = 'none';
        ['mat-metallic','mat-roughness','mat-alpha','mat-transmission'].forEach(id => {
            const el = document.getElementById(id);
            if (el) document.getElementById(id+'-val').textContent = el.value+'%';
        });
    }

    modal.style.display = 'flex';
}

function closeModal() {
    document.getElementById('material-modal').style.display = 'none';
    editingId = null;
}

function setRange(id, val) {
    const el = document.getElementById(id);
    el.value = Math.round(val);
    document.getElementById(id + '-val').textContent = Math.round(val) + '%';
}

async function saveMaterial() {
    const hex = document.getElementById('mat-color').value;
    const rgb = hexToRgb(hex);
    const alpha = parseInt(document.getElementById('mat-alpha').value) / 100;

    let finalCategory = document.getElementById('mat-category').value;
    if (finalCategory === 'custom') {
        finalCategory = document.getElementById('mat-category-custom').value.trim().toLowerCase() || 'other';
    }

    const payload = {
        material_id: document.getElementById('mat-id').value.trim(),
        name: document.getElementById('mat-name').value.trim(),
        category: finalCategory,
        tags: document.getElementById('mat-tags').value.split(',').map(t => t.trim()).filter(Boolean),
        description: document.getElementById('mat-desc').value.trim() || null,
        pbr_properties: {
            base_color: [rgb.r/255, rgb.g/255, rgb.b/255, alpha],
            metallic: parseInt(document.getElementById('mat-metallic').value) / 100,
            roughness: parseInt(document.getElementById('mat-roughness').value) / 100,
            alpha: alpha,
            ior: parseFloat(document.getElementById('mat-ior').value),
            transmission: parseInt(document.getElementById('mat-transmission').value) / 100,
            emission: 0,
            // Add generated maps safely (only the map paths)
            ...(currentGeneratedMaps ? {
                base_color_map: currentGeneratedMaps.base_color_map,
                normal_map: currentGeneratedMaps.normal_map,
                roughness_map: currentGeneratedMaps.roughness_map,
                displacement_map: currentGeneratedMaps.displacement_map,
                metallic_map: currentGeneratedMaps.metallic_map
            } : {})
        }
    };

    console.log('Final Material Payload:', payload);

    try {
        let res;
        if (editingId) {
            // Update
            const updatePayload = { ...payload };
            delete updatePayload.material_id;
            res = await fetch(`/materials/${editingId}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(updatePayload),
            });
        } else {
            // Create
            res = await fetch('/materials', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload),
            });
        }
        if (!res.ok) {
            const err = await res.json();
            alert(err.detail || 'Erro ao salvar material');
            return;
        }
        closeModal();
        await loadMaterials();
    } catch (e) {
        alert('Erro de conexão: ' + e.message);
    }
}

async function deleteMaterial(id, name) {
    if (!confirm(`Excluir "${name}"?`)) return;
    try {
        const res = await fetch(`/materials/${id}`, { method: 'DELETE' });
        if (res.ok) {
            selectedIds.delete(id);
            _onSelectionChange([...selectedIds]);
            await loadMaterials();
        }
    } catch (e) { console.error(e); }
}

// ─── Helpers ────────────────────────────────────────────────────

function rgbToHex(r, g, b) {
    const toHex = v => Math.round(v * 255).toString(16).padStart(2, '0');
    return `#${toHex(r)}${toHex(g)}${toHex(b)}`;
}

function hexToRgb(hex) {
    const n = parseInt(hex.slice(1), 16);
    return { r: (n >> 16) & 255, g: (n >> 8) & 255, b: n & 255 };
}

export function getMaterialById(id) {
    return allMaterials.find(m => m.material_id === id);
}

// ─── Modal Tab Switching ─────────────────────────────────────────

function switchModalTab(tab) {
    const manualTab = document.getElementById('modal-tab-manual');
    const polyHavenTab = document.getElementById('modal-tab-polyhaven');
    const manualBtn = document.getElementById('tab-btn-manual');
    const phBtn = document.getElementById('tab-btn-polyhaven');

    if (tab === 'manual') {
        manualTab.style.display = 'block';
        polyHavenTab.style.display = 'none';
        manualBtn.classList.add('active');
        phBtn.classList.remove('active');
    } else {
        manualTab.style.display = 'none';
        polyHavenTab.style.display = 'block';
        manualBtn.classList.remove('active');
        phBtn.classList.add('active');
    }
}

// ─── Poly Haven Integration ──────────────────────────────────────

function _bindPHSearch() {
    const phInput = document.getElementById('ph-search-input');
    if (phInput) {
        phInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                e.preventDefault();
                searchPolyHaven();
            }
        });
    }
}

async function searchPolyHaven() {
    const qInput = document.getElementById('ph-search-input');
    const q = qInput.value;
    const resultsDiv = document.getElementById('ph-results');
    
    if (!q.trim()) {
        alert('Digite algo para buscar');
        return;
    }

    resultsDiv.innerHTML = '<div style="grid-column: 1/-1; text-align: center; padding: 2rem;"><div class="viewer-spinner" style="margin: 0 auto; width: 30px; height: 30px;"></div><p style="margin-top: 1rem; font-size: 0.8rem;">Buscando biblioteca...</p></div>';
    
    try {
        const res = await fetch(`/materials/polyhaven/search?q=${encodeURIComponent(q)}`);
        const data = await res.json();
        
        if (data.length === 0) {
            resultsDiv.innerHTML = '<div style="grid-column: 1/-1; text-align: center; padding: 2rem; color: var(--text-muted);">Nenhum resultado encontrado para essa busca.</div>';
            return;
        }
        
        resultsDiv.innerHTML = data.map(asset => `
            <div class="ph-asset-card">
                <img src="${asset.thumbnail}" class="ph-asset-img" loading="lazy">
                <div class="ph-asset-info">
                    <div class="ph-asset-name" title="${asset.name}">
                        ${asset.name}
                    </div>
                    <button class="ph-import-btn" onclick="importPolyHaven('${asset.id}', this)">
                        📥 Importar
                    </button>
                </div>
            </div>
        `).join('');
    } catch (err) {
        resultsDiv.innerHTML = `<div style="grid-column: 1/-1; text-align: center; padding: 2rem; color: #e74c3c;">Erro na API: ${err.message}</div>`;
    }
}

async function importPolyHaven(assetId, btn) {
    const originalHtml = btn.innerHTML;
    const resValue = document.getElementById('ph-res').value;
    
    btn.disabled = true;
    btn.innerHTML = '<div class="viewer-spinner" style="width: 12px; height: 12px; border-width: 2px; margin: 0 auto;"></div>';
    
    try {
        const formData = new FormData();
        formData.append('asset_id', assetId);
        formData.append('resolution', resValue);
        
        const res = await fetch('/materials/polyhaven/import', {
            method: 'POST',
            body: formData
        });
        
        if (!res.ok) throw new Error('Falha ao baixar mapas PBR');
        
        const data = await res.json();
        
        btn.innerHTML = '✅ PRONTO';
        btn.style.background = 'var(--success)';
        
        // Refresh materials list
        if (typeof loadMaterials === 'function') await loadMaterials();
        
        // Success feedback and close
        setTimeout(() => {
            closeModal();
            btn.disabled = false;
            btn.innerHTML = originalHtml;
            btn.style.background = '';
        }, 1000);
        
    } catch (err) {
        alert('Erro ao importar: ' + err.message);
        btn.disabled = false;
        btn.innerHTML = originalHtml;
    }
}

// Global scope expose
window.searchPolyHaven = searchPolyHaven;
window.importPolyHaven = importPolyHaven;
window.switchModalTab = switchModalTab;
window.closeModal = closeModal;
window.saveMaterial = saveMaterial;
window.openModal = openModal;
