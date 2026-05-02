document.addEventListener('DOMContentLoaded', () => {
    const dropzone = document.getElementById('dropzone');
    const fileInput = document.getElementById('file-input');
    const fileInfo = document.getElementById('file-info');
    const filenameLabel = document.getElementById('filename');
    const filesizeLabel = document.getElementById('filesize');
    const btnRender = document.getElementById('btn-render');
    const jobsList = document.getElementById('jobs-list');
    const gallery = document.getElementById('results-gallery');
    const noResults = document.getElementById('no-results');

    let selectedFile = null;
    let activeJobs = new Set();

    // --- Drag and Drop ---

    dropzone.addEventListener('click', () => fileInput.click());

    dropzone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropzone.classList.add('active');
    });

    dropzone.addEventListener('dragleave', () => {
        dropzone.classList.remove('active');
    });

    dropzone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropzone.classList.remove('active');
        handleFiles(e.dataTransfer.files);
    });

    fileInput.addEventListener('change', (e) => {
        handleFiles(e.target.files);
    });

    function handleFiles(files) {
        if (files.length === 0) return;
        
        const file = files[0];
        const ext = file.name.split('.').pop().toLowerCase();
        
        if (!['glb', 'gltf', 'obj', 'dae', 'skp'].includes(ext)) {
            alert(`Formato não suportado! Use apenas .glb, .gltf, .obj, .dae ou .skp.`);
            return;
        }

        selectedFile = file;
        filenameLabel.textContent = file.name;
        filesizeLabel.textContent = `${(file.size / (1024 * 1024)).toFixed(2)} MB`;
        fileInfo.style.display = 'block';
        btnRender.disabled = false;
        
        // Visual feedback
        dropzone.style.borderColor = 'var(--success)';
        dropzone.querySelector('p').innerHTML = `Pronto para renderizar: <strong>${file.name}</strong>`;
    }

    // --- Render Submission ---

    btnRender.addEventListener('click', async () => {
        if (!selectedFile) return;

        const formData = new FormData();
        formData.append('file', selectedFile);
        formData.append('samples', document.getElementById('samples').value);
        formData.append('resolution_x', document.getElementById('res-x').value);
        formData.append('resolution_y', document.getElementById('res-y').value);
        formData.append('device', document.getElementById('device').value);
        formData.append('camera_angle', document.getElementById('camera').value);

        btnRender.disabled = true;
        btnRender.textContent = 'Enviando...';

        try {
            const response = await fetch('/render', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Falha ao enviar arquivo');
            }

            const data = await response.json();
            addJobToList(data.job_id, selectedFile.name);
            
            // Reset UI
            selectedFile = null;
            btnRender.textContent = 'Iniciar Renderização';
            fileInfo.style.display = 'none';
            dropzone.style.borderColor = 'var(--border)';
            dropzone.querySelector('p').innerHTML = 'Arraste seu arquivo <strong>.glb</strong> ou <strong>.gltf</strong> aqui';
        } catch (error) {
            alert(`Erro: ${error.message}`);
            btnRender.disabled = false;
            btnRender.textContent = 'Iniciar Renderização';
        }
    });

    // --- Job Tracking ---

    function addJobToList(jobId, filename) {
        if (activeJobs.has(jobId)) return;
        activeJobs.add(jobId);

        const jobEl = document.createElement('div');
        jobEl.className = 'job-item fade-in';
        jobEl.id = `job-${jobId}`;
        jobEl.innerHTML = `
            <div class="job-header">
                <strong>${filename}</strong>
                <span class="job-status status-pending">Pendente</span>
            </div>
            <div class="progress-bar">
                <div class="progress-fill" style="width: 0%"></div>
            </div>
            <p style="font-size: 0.7rem; color: var(--text-dim); margin-top: 0.5rem;">ID: ${jobId}</p>
        `;

        jobsList.prepend(jobEl);
        pollStatus(jobId);
    }

    async function pollStatus(jobId) {
        const jobEl = document.getElementById(`job-${jobId}`);
        const statusBadge = jobEl.querySelector('.job-status');
        const progressFill = jobEl.querySelector('.progress-fill');

        const interval = setInterval(async () => {
            try {
                const response = await fetch(`/render/status/${jobId}`);
                const data = await response.json();

                // Update UI based on status
                statusBadge.textContent = data.status;
                statusBadge.className = `job-status status-${data.status}`;
                
                if (data.progress) {
                    progressFill.style.width = `${data.progress}%`;
                }

                if (data.status === 'completed') {
                    clearInterval(interval);
                    progressFill.style.width = '100%';
                    addToGallery(jobId);
                    activeJobs.delete(jobId);
                    setTimeout(() => jobEl.remove(), 5000); // Remove from list after 5s
                } else if (data.status === 'failed') {
                    clearInterval(interval);
                    alert(`Job ${jobId} falhou: ${data.error}`);
                    activeJobs.delete(jobId);
                }
            } catch (err) {
                console.error('Erro ao verificar status:', err);
            }
        }, 2000);
    }

    // --- Gallery ---

    function addToGallery(jobId) {
        noResults.style.display = 'none';
        
        const card = document.createElement('div');
        card.className = 'render-card fade-in';
        card.innerHTML = `
            <img src="/render/download/${jobId}" alt="Render result">
            <div class="render-info">
                <span>Job ${jobId.slice(0, 8)}...</span>
                <a href="/render/download/${jobId}" class="download-link" download="render_${jobId}.png">Download</a>
            </div>
        `;
        
        gallery.prepend(card);
    }

    // Initial check for storage
    async function checkStatus() {
        try {
            const res = await fetch('/health');
            const data = await res.json();
            if (data.status === 'healthy') {
                document.getElementById('api-status').textContent = 'Online';
            }
        } catch (e) {
            document.getElementById('api-status').textContent = 'Offline';
            document.getElementById('api-status').className = 'job-status status-failed';
        }
    }

    checkStatus();
});
