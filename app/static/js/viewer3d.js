/**
 * Frank 3D Preview Viewer
 * 
 * Interactive Three.js viewer for previewing GLB/GLTF models
 * before submitting to the Blender Cycles render pipeline.
 * 
 * Provides orbit controls, camera presets, and exports camera
 * parameters (position, rotation, FOV) in Blender-compatible format.
 */

import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { OBJLoader } from 'three/addons/loaders/OBJLoader.js';
import { MTLLoader } from 'three/addons/loaders/MTLLoader.js';
import { ColladaLoader } from 'three/addons/loaders/ColladaLoader.js';

// ─── Coordinate System Conversion ───────────────────────────────
// Three.js: Y-up, right-handed
// Blender:  Z-up, right-handed
// Conversion: swap Y and Z, negate new Y (Blender's Y = -Three.js Z)

function threeToBlenderPosition(threePos) {
    return [threePos.x, -threePos.z, threePos.y];
}

function threeToBlenderRotation(camera) {
    // Extract camera direction and up vectors, convert to Blender Euler
    // We send the raw Three.js values and let the Blender script handle conversion
    // using the same track_quat approach it already uses
    const dir = new THREE.Vector3();
    camera.getWorldDirection(dir);
    
    // Convert direction to Blender space
    const blenderDir = [dir.x, -dir.z, dir.y];
    
    return blenderDir;
}

// ─── Animation Helper ───────────────────────────────────────────

function animateValue(obj, prop, target, duration, easing) {
    const start = typeof obj[prop] === 'object' ? obj[prop].clone() : obj[prop];
    const startTime = performance.now();
    
    return new Promise(resolve => {
        function update(currentTime) {
            const elapsed = currentTime - startTime;
            const t = Math.min(elapsed / duration, 1);
            const ease = easing ? easing(t) : easeOutCubic(t);
            
            if (typeof start === 'object' && start.isVector3) {
                obj[prop].lerpVectors(start, target, ease);
            } else {
                obj[prop] = start + (target - start) * ease;
            }
            
            if (t < 1) {
                requestAnimationFrame(update);
            } else {
                resolve();
            }
        }
        requestAnimationFrame(update);
    });
}

function easeOutCubic(t) {
    return 1 - Math.pow(1 - t, 3);
}

// ─── Main Viewer Class ──────────────────────────────────────────

export class Frank3DViewer {
    constructor(containerId) {
        this.container = document.getElementById(containerId);
        if (!this.container) {
            throw new Error(`Container #${containerId} not found`);
        }
        
        this.scene = null;
        this.camera = null;
        this.renderer = null;
        this.controls = null;
        this.model = null;
        this.gridHelper = null;
        this.animationId = null;
        this.modelCenter = new THREE.Vector3();
        this.modelSize = 1;
        
        // Camera info callback
        this.onCameraChange = null;
        
        this._init();
    }
    
    _init() {
        const width = this.container.clientWidth;
        const height = this.container.clientHeight || 400;
        
        // Scene
        this.scene = new THREE.Scene();
        this.scene.background = new THREE.Color(0x0d0d10);
        
        // Camera
        this.camera = new THREE.PerspectiveCamera(60, width / height, 0.01, 10000);
        this.camera.position.set(5, 3, 5);
        
        // Renderer
        this.renderer = new THREE.WebGLRenderer({
            antialias: true,
            alpha: false,
            powerPreference: 'high-performance',
        });
        this.renderer.setSize(width, height);
        this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
        this.renderer.toneMapping = THREE.ACESFilmicToneMapping;
        this.renderer.toneMappingExposure = 1.2;
        this.renderer.shadowMap.enabled = true;
        this.renderer.shadowMap.type = THREE.PCFSoftShadowMap;
        this.container.appendChild(this.renderer.domElement);
        
        // Controls
        this.controls = new OrbitControls(this.camera, this.renderer.domElement);
        this.controls.enableDamping = true;
        this.controls.dampingFactor = 0.08;
        this.controls.rotateSpeed = 0.8;
        this.controls.zoomSpeed = 1.2;
        this.controls.panSpeed = 0.8;
        this.controls.minDistance = 0.1;
        this.controls.maxDistance = 1000;
        
        // Fire camera change events
        this.controls.addEventListener('change', () => {
            if (this.onCameraChange) {
                this.onCameraChange(this.getCameraParams());
            }
        });
        
        // Lighting (matches Blender 3-point setup)
        this._setupLighting();
        
        // Grid
        this._setupGrid();
        
        // Fog for depth
        this.scene.fog = new THREE.FogExp2(0x0d0d10, 0.015);
        
        // Resize handler
        this._resizeObserver = new ResizeObserver(() => this._onResize());
        this._resizeObserver.observe(this.container);
        
        // Start render loop
        this._animate();
    }
    
    _setupLighting() {
        // Ambient
        const ambient = new THREE.AmbientLight(0xffffff, 0.3);
        this.scene.add(ambient);
        
        // Key Light (warm, strong, upper right)
        const keyLight = new THREE.DirectionalLight(0xfff0e0, 1.5);
        keyLight.position.set(5, 8, 4);
        keyLight.castShadow = true;
        keyLight.shadow.mapSize.width = 2048;
        keyLight.shadow.mapSize.height = 2048;
        this.scene.add(keyLight);
        this._keyLight = keyLight;
        
        // Fill Light (cool, soft, left)
        const fillLight = new THREE.DirectionalLight(0xe0e8ff, 0.6);
        fillLight.position.set(-4, 3, -2);
        this.scene.add(fillLight);
        this._fillLight = fillLight;
        
        // Rim Light (behind, for edge separation)
        const rimLight = new THREE.DirectionalLight(0xffffff, 0.8);
        rimLight.position.set(-2, 6, -5);
        this.scene.add(rimLight);
        this._rimLight = rimLight;
        
        // Hemisphere light for natural ambient
        const hemiLight = new THREE.HemisphereLight(0xddeeff, 0x202020, 0.4);
        this.scene.add(hemiLight);
    }
    
    _setupGrid() {
        // Subtle grid on the floor
        this.gridHelper = new THREE.GridHelper(20, 20, 0x333340, 0x1a1a22);
        this.gridHelper.material.opacity = 0.4;
        this.gridHelper.material.transparent = true;
        this.scene.add(this.gridHelper);
        
        // Ground plane for shadow reception
        const groundGeo = new THREE.PlaneGeometry(50, 50);
        const groundMat = new THREE.ShadowMaterial({ opacity: 0.15 });
        const ground = new THREE.Mesh(groundGeo, groundMat);
        ground.rotation.x = -Math.PI / 2;
        ground.position.y = -0.01;
        ground.receiveShadow = true;
        this.scene.add(ground);
    }
    
    _onResize() {
        const width = this.container.clientWidth;
        const height = this.container.clientHeight;
        
        this.camera.aspect = width / height;
        this.camera.updateProjectionMatrix();
        this.renderer.setSize(width, height);
    }
    
    _animate() {
        this.animationId = requestAnimationFrame(() => this._animate());
        this.controls.update();
        this.renderer.render(this.scene, this.camera);
    }
    
    // ─── Model Loading ──────────────────────────────────────────
    
    async loadFromFile(file, additionalFiles = []) {
        // Remove previous model
        if (this.model) {
            this.scene.remove(this.model);
            this.model = null;
        }

        const ext = file.name.split('.').pop().toLowerCase();
        const url = URL.createObjectURL(file);

        try {
            switch (ext) {
                case 'glb':
                case 'gltf':
                    await this._loadGLTF(url);
                    break;
                case 'obj':
                    await this._loadOBJ(url, file, additionalFiles);
                    break;
                case 'dae':
                    await this._loadCollada(url, file);
                    break;
                default:
                    URL.revokeObjectURL(url);
                    throw new Error(`Formato .${ext} não suportado para preview`);
            }
        } catch (err) {
            URL.revokeObjectURL(url);
            throw err;
        }
    }

    _loadGLTF(url) {
        return new Promise((resolve, reject) => {
            const loader = new GLTFLoader();
            loader.load(
                url,
                (gltf) => {
                    this.model = gltf.scene;
                    this._processLoadedModel();
                    URL.revokeObjectURL(url);
                    resolve();
                },
                (progress) => {
                    if (progress.total > 0) {
                        console.log(`[Frank3D] Loading GLTF: ${((progress.loaded / progress.total) * 100).toFixed(0)}%`);
                    }
                },
                (error) => {
                    URL.revokeObjectURL(url);
                    reject(error);
                }
            );
        });
    }

    _loadOBJ(url, file, additionalFiles = []) {
        return new Promise((resolve, reject) => {
            const mtlFile = additionalFiles.find(f => f.name.toLowerCase().endsWith('.mtl'));
            
            const parseOBJ = (materials = null) => {
                const reader = new FileReader();
                reader.onload = (e) => {
                    try {
                        const loader = new OBJLoader();
                        if (materials) {
                            loader.setMaterials(materials);
                        }
                        this.model = loader.parse(e.target.result);

                        // Apply default PBR material to meshes without proper materials
                        this.model.traverse((child) => {
                            if (child.isMesh) {
                                if (!child.material || child.material.type === 'MeshBasicMaterial' ||
                                    (child.material.type === 'MeshPhongMaterial' && !child.material.map)) {
                                    
                                    // Preserve the material name parsed from the OBJ/MTL
                                    const originalName = child.material ? child.material.name : child.name;
                                    
                                    child.material = new THREE.MeshStandardMaterial({
                                        name: originalName, // VERY IMPORTANT: Keep the name so we can match it later!
                                        color: 0x999999,
                                        roughness: 0.5,
                                        metalness: 0.1,
                                    });
                                }
                            }
                        });

                        this._processLoadedModel();
                        URL.revokeObjectURL(url);
                        resolve();
                    } catch (err) {
                        URL.revokeObjectURL(url);
                        reject(err);
                    }
                };
                reader.onerror = () => {
                    URL.revokeObjectURL(url);
                    reject(new Error('Falha ao ler arquivo OBJ'));
                };
                reader.readAsText(file);
            };

            if (mtlFile) {
                const mtlReader = new FileReader();
                mtlReader.onload = (e) => {
                    try {
                        const mtlLoader = new MTLLoader();
                        const materials = mtlLoader.parse(e.target.result);
                        materials.preload();
                        parseOBJ(materials);
                    } catch (err) {
                        console.warn('[Frank3D] Failed to parse MTL, loading OBJ without materials', err);
                        parseOBJ();
                    }
                };
                mtlReader.onerror = () => parseOBJ();
                mtlReader.readAsText(mtlFile);
            } else {
                parseOBJ();
            }
        });
    }

    _loadCollada(url, file) {
        return new Promise((resolve, reject) => {
            // Read file as text and use parse() to avoid blob URL MIME issues
            const reader = new FileReader();
            reader.onload = (e) => {
                try {
                    const loader = new ColladaLoader();
                    const collada = loader.parse(e.target.result);
                    this.model = collada.scene;
                    this._processLoadedModel();
                    URL.revokeObjectURL(url);
                    resolve();
                } catch (err) {
                    URL.revokeObjectURL(url);
                    reject(err);
                }
            };
            reader.onerror = () => {
                URL.revokeObjectURL(url);
                reject(new Error('Falha ao ler arquivo DAE'));
            };
            reader.readAsText(file);
        });
    }

    _processLoadedModel() {
        if (!this.model) return;

        this.structure = [];
        const uniqueNames = new Set();
        this.originalMaterials = new Map(); // Store original materials for highlighting

        // Enable shadows and collect structure
        this.model.traverse((child) => {
            if (child.isMesh) {
                child.castShadow = true;
                child.receiveShadow = true;
                
                // Save original material for highlighting
                this.originalMaterials.set(child.uuid, child.material);

                if (child.name && !uniqueNames.has(child.name)) {
                    uniqueNames.add(child.name);
                    
                    // Get material name (handle arrays for multi-materials)
                    let matName = null;
                    if (child.material) {
                        if (Array.isArray(child.material)) {
                            matName = child.material[0].name;
                        } else {
                            matName = child.material.name;
                        }
                    }

                    this.structure.push({
                        name: child.name,
                        type: 'mesh',
                        materialName: matName
                    });
                }
            }
        });

        // If no named meshes found, try to use top-level children
        if (this.structure.length === 0) {
            this.model.children.forEach(child => {
                if (child.name) {
                    this.structure.push({
                        name: child.name,
                        type: child.isMesh ? 'mesh' : 'group'
                    });
                }
            });
        }

        this.scene.add(this.model);

        // Calculate bounds and auto-frame
        this._fitModelInView();
    }

    highlightPart(name) {
        if (!this.model) return;
        
        const highlightColor = new THREE.Color(0x3498db); // Frank Blue
        
        this.model.traverse((child) => {
            if (child.isMesh) {
                if (child.name === name || (child.parent && child.parent.name === name)) {
                    // Highlight match
                    if (!child.material._isHighlight) {
                        const oldMat = this.originalMaterials.get(child.uuid);
                        if (oldMat) {
                            if (Array.isArray(oldMat)) {
                                child.material = oldMat.map(m => m.clone());
                            } else {
                                child.material = oldMat.clone();
                            }
                            
                            // Mark as highlight material to avoid re-cloning
                            if (Array.isArray(child.material)) {
                                child.material.forEach(m => m._isHighlight = true);
                            } else {
                                child.material._isHighlight = true;
                            }
                        }
                    }
                    
                    const mats = Array.isArray(child.material) ? child.material : [child.material];
                    mats.forEach(m => {
                        if (m.emissive) {
                            m.emissive.set(highlightColor);
                            m.emissiveIntensity = 0.5;
                        } else {
                            m.transparent = true;
                            m.opacity = 0.7;
                        }
                    });
                } else {
                    // Dim others
                    const mats = Array.isArray(child.material) ? child.material : [child.material];
                    mats.forEach(m => {
                        if (m.emissive) {
                            m.emissive.set(0x000000);
                            m.emissiveIntensity = 0;
                        }
                        m.transparent = true;
                        m.opacity = 0.3;
                    });
                }
            }
        });
    }

    clearHighlight() {
        if (!this.model) return;
        this.model.traverse((child) => {
            if (child.isMesh) {
                const original = this.originalMaterials.get(child.uuid);
                if (original) {
                    child.material = original;
                    // Reset transparency if it was modified on the original material (unlikely but safe)
                    if (Array.isArray(original)) {
                        original.forEach(m => {
                            m.transparent = m.transparent; // This just forces a refresh if needed
                        });
                    }
                }
            }
        });
    }

    setPartMaterial(name, pbrProps) {
        if (!this.model) return;
        
        this.model.traverse((child) => {
            if (child.isMesh) {
                if (child.name === name || (child.parent && child.parent.name === name)) {
                    // Create a new material
                    const bc = pbrProps.base_color || [0.7, 0.7, 0.7, 1];
                    const colorStr = `rgb(${Math.round(bc[0]*255)},${Math.round(bc[1]*255)},${Math.round(bc[2]*255)})`;
                    
                    const newMat = new THREE.MeshStandardMaterial({
                        color: new THREE.Color(colorStr),
                        metalness: pbrProps.metallic !== undefined ? pbrProps.metallic : 0.0,
                        roughness: pbrProps.roughness !== undefined ? pbrProps.roughness : 0.5
                    });
                    
                    // We need to keep the original for resetPartMaterial
                    if (!this.importedMaterials) {
                        this.importedMaterials = new Map();
                    }
                    if (!this.importedMaterials.has(child.uuid)) {
                        this.importedMaterials.set(child.uuid, this.originalMaterials.get(child.uuid));
                    }
                    
                    child.material = newMat;
                    // Update originalMaterials so clearHighlight restores this new material
                    this.originalMaterials.set(child.uuid, newMat);
                }
            }
        });
    }

    resetPartMaterial(name) {
        if (!this.model || !this.importedMaterials) return;
        
        this.model.traverse((child) => {
            if (child.isMesh) {
                if (child.name === name || (child.parent && child.parent.name === name)) {
                    const imported = this.importedMaterials.get(child.uuid);
                    if (imported) {
                        child.material = imported;
                        this.originalMaterials.set(child.uuid, imported);
                    }
                }
            }
        });
    }

    getModelStructure() {
        return this.structure || [];
    }
    
    _fitModelInView() {
        if (!this.model) return;
        
        const box = new THREE.Box3().setFromObject(this.model);
        const center = box.getCenter(new THREE.Vector3());
        const size = box.getSize(new THREE.Vector3());
        
        this.modelCenter.copy(center);
        this.modelSize = Math.max(size.x, size.y, size.z);
        
        if (this.modelSize === 0) this.modelSize = 2;
        
        // Update grid scale based on model
        const gridSize = this.modelSize * 3;
        this.scene.remove(this.gridHelper);
        this.gridHelper = new THREE.GridHelper(gridSize, 20, 0x333340, 0x1a1a22);
        this.gridHelper.material.opacity = 0.4;
        this.gridHelper.material.transparent = true;
        this.gridHelper.position.y = box.min.y;
        this.scene.add(this.gridHelper);
        
        // Update light positions based on model size
        const d = this.modelSize * 2.5;
        this._keyLight.position.set(center.x + d * 0.7, center.y + d * 0.8, center.z + d * 0.5);
        this._fillLight.position.set(center.x - d * 0.6, center.y + d * 0.4, center.z - d * 0.3);
        this._rimLight.position.set(center.x - d * 0.3, center.y + d * 0.9, center.z - d * 0.6);
        
        // Update camera clipping
        this.camera.near = this.modelSize * 0.001;
        this.camera.far = this.modelSize * 100;
        this.camera.updateProjectionMatrix();
        
        // Update fog
        this.scene.fog = new THREE.FogExp2(0x0d0d10, 0.3 / this.modelSize);
        
        // Update controls
        this.controls.target.copy(center);
        this.controls.minDistance = this.modelSize * 0.1;
        this.controls.maxDistance = this.modelSize * 20;
        
        // Set camera to perspective preset
        this.setCameraPreset('perspective', false);
        
        // Trigger camera change
        if (this.onCameraChange) {
            this.onCameraChange(this.getCameraParams());
        }
    }
    
    // ─── Camera Presets ─────────────────────────────────────────
    
    setCameraPreset(preset, animate = true) {
        const center = this.modelCenter;
        const d = this.modelSize * 2.0;
        
        const presets = {
            perspective: new THREE.Vector3(
                center.x + d * 0.7,
                center.y + d * 0.5,
                center.z + d * 0.7
            ),
            front: new THREE.Vector3(
                center.x,
                center.y,
                center.z + d
            ),
            top: new THREE.Vector3(
                center.x,
                center.y + d * 1.5,
                center.z + 0.01  // slight offset to avoid gimbal lock
            ),
            side: new THREE.Vector3(
                center.x + d,
                center.y,
                center.z
            ),
            back: new THREE.Vector3(
                center.x,
                center.y,
                center.z - d
            ),
        };
        
        const targetPos = presets[preset] || presets.perspective;
        
        if (animate) {
            this._animateCamera(targetPos, center);
        } else {
            this.camera.position.copy(targetPos);
            this.controls.target.copy(center);
            this.controls.update();
        }
    }
    
    _animateCamera(targetPos, targetLookAt) {
        const startPos = this.camera.position.clone();
        const startTarget = this.controls.target.clone();
        const duration = 600;
        const startTime = performance.now();
        
        const animate = (now) => {
            const elapsed = now - startTime;
            const t = Math.min(elapsed / duration, 1);
            const ease = easeOutCubic(t);
            
            this.camera.position.lerpVectors(startPos, targetPos, ease);
            this.controls.target.lerpVectors(startTarget, targetLookAt, ease);
            this.controls.update();
            
            if (t < 1) {
                requestAnimationFrame(animate);
            } else {
                if (this.onCameraChange) {
                    this.onCameraChange(this.getCameraParams());
                }
            }
        };
        
        requestAnimationFrame(animate);
    }
    
    // ─── Camera Parameters ──────────────────────────────────────
    
    getCameraParams() {
        const pos = this.camera.position;
        const rot = this.camera.rotation;
        const target = this.controls.target;
        
        // Direction vector (where camera is looking)
        const direction = new THREE.Vector3();
        this.camera.getWorldDirection(direction);
        
        return {
            // Three.js coordinates (for display)
            position: { x: pos.x, y: pos.y, z: pos.z },
            rotation: { x: rot.x, y: rot.y, z: rot.z },
            target: { x: target.x, y: target.y, z: target.z },
            fov: this.camera.fov,
            
            // Blender-compatible coordinates (for render submission)
            blender: {
                position: threeToBlenderPosition(pos),
                target: threeToBlenderPosition(target),
                direction: threeToBlenderRotation(this.camera),
                fov: this.camera.fov,
            }
        };
    }
    
    setFOV(fov) {
        this.camera.fov = Math.max(10, Math.min(120, fov));
        this.camera.updateProjectionMatrix();
        
        if (this.onCameraChange) {
            this.onCameraChange(this.getCameraParams());
        }
    }

    setCameraParams(params) {
        if (!this.model) return;
        
        if (params.position) {
            this.camera.position.set(params.position.x, params.position.y, params.position.z);
        }
        if (params.target) {
            this.controls.target.set(params.target.x, params.target.y, params.target.z);
        }
        
        this.controls.update();
        
        if (this.onCameraChange) {
            this.onCameraChange(this.getCameraParams());
        }
    }

    setControlSpeed(multiplier = 1.0) {
        if (!this.controls) return;
        this.controls.rotateSpeed = 0.8 * multiplier;
        this.controls.zoomSpeed = 1.2 * multiplier;
        this.controls.panSpeed = 0.8 * multiplier;
    }
    
    resetCamera() {
        this.setCameraPreset('perspective', true);
    }
    
    // ─── Cleanup ────────────────────────────────────────────────
    
    dispose() {
        if (this.animationId) {
            cancelAnimationFrame(this.animationId);
        }
        
        if (this._resizeObserver) {
            this._resizeObserver.disconnect();
        }
        
        if (this.controls) {
            this.controls.dispose();
        }
        
        if (this.renderer) {
            this.renderer.dispose();
            if (this.renderer.domElement.parentNode) {
                this.renderer.domElement.parentNode.removeChild(this.renderer.domElement);
            }
        }
        
        // Dispose of scene objects
        if (this.scene) {
            this.scene.traverse((object) => {
                if (object.geometry) object.geometry.dispose();
                if (object.material) {
                    if (Array.isArray(object.material)) {
                        object.material.forEach(mat => mat.dispose());
                    } else {
                        object.material.dispose();
                    }
                }
            });
        }
    }
}
