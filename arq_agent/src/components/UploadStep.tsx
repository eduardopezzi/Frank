import React, { useState } from 'react'
import { Upload as UploadIcon, X } from 'lucide-react'

interface UploadStepProps {
    onImageSelected: (base64: string) => void;
    onNext: () => void;
}

export const UploadStep: React.FC<UploadStepProps> = ({ onImageSelected, onNext }) => {
    const [preview, setPreview] = useState<string | null>(null)

    const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const file = e.target.files?.[0]
        if (file) {
            const reader = new FileReader()
            reader.onloadend = () => {
                const base64 = reader.result as string
                setPreview(base64)
                onImageSelected(base64)
            }
            reader.readAsDataURL(file)
        }
    }

    return (
        <div className="glass-card fade-in">
            <h2>Upload do SketchUp</h2>
            <p style={{ color: 'var(--text-secondary)', marginBottom: '2rem' }}>
                Arraste ou selecione o print do seu projeto 3D no SketchUp para análise.
            </p>

            <div
                style={{
                    border: '2px dashed var(--glass-border)',
                    borderRadius: '12px',
                    padding: '3rem',
                    textAlign: 'center',
                    cursor: 'pointer',
                    position: 'relative',
                    background: preview ? 'none' : 'rgba(255,255,255,0.02)',
                    minHeight: '300px',
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    justifyContent: 'center'
                }}
                onClick={() => !preview && document.getElementById('fileInput')?.click()}
            >
                {preview ? (
                    <div style={{ width: '100%', position: 'relative' }}>
                        <img
                            src={preview}
                            alt="Preview"
                            style={{ width: '100%', borderRadius: '8px', maxHeight: '400px', objectFit: 'contain' }}
                        />
                        <button
                            onClick={(e) => { e.stopPropagation(); setPreview(null); }}
                            style={{
                                position: 'absolute', top: '-10px', right: '-10px',
                                background: '#ff4b2b', color: 'white', border: 'none',
                                borderRadius: '50%', padding: '4px', cursor: 'pointer'
                            }}
                        >
                            <X size={16} />
                        </button>
                    </div>
                ) : (
                    <>
                        <UploadIcon size={48} color="var(--accent-color)" style={{ marginBottom: '1rem' }} />
                        <p>Clique aqui para selecionar uma imagem</p>
                        <span style={{ fontSize: '0.8rem', color: 'var(--text-secondary)' }}>JPG, PNG ou WEBP</span>
                    </>
                )}
                <input
                    id="fileInput"
                    type="file"
                    hidden
                    accept="image/*"
                    onChange={handleFileChange}
                />
            </div>

            <div style={{ marginTop: '2rem', display: 'flex', justifyContent: 'space-between' }}>
                <p style={{ color: 'var(--text-secondary)', fontSize: '0.8rem' }}>
                    Dica: Use uma vista clara com boa visibilidade dos materiais.
                </p>
                <button
                    className="btn-primary"
                    disabled={!preview}
                    onClick={onNext}
                >
                    Analisar Elementos
                </button>
            </div>
        </div>
    )
}
