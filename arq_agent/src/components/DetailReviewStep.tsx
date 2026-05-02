import React, { useState, useRef } from 'react'
import { Plus, Trash2, Check, Loader2, Image as ImageIcon, X } from 'lucide-react'
import type { Detail } from '../services/gemini'

interface DetailReviewStepProps {
    details: Detail[];
    isLoading: boolean;
    onUpdate: (index: number, updated: Partial<Detail>) => void;
    onAdd: (text: string) => void;
    onRemove: (index: number) => void;
    onNext: () => void;
}

export const DetailReviewStep: React.FC<DetailReviewStepProps> = ({
    details, isLoading, onUpdate, onAdd, onRemove, onNext
}) => {
    const [newDetail, setNewDetail] = useState('')
    const fileInputRef = useRef<HTMLInputElement>(null)
    const [activeUploadIndex, setActiveUploadIndex] = useState<number | null>(null)

    const handleAdd = () => {
        if (newDetail.trim()) {
            onAdd(newDetail.trim())
            setNewDetail('')
        }
    }

    const handleImageUpload = (index: number, e: React.ChangeEvent<HTMLInputElement>) => {
        const file = e.target.files?.[0]
        if (file) {
            const reader = new FileReader()
            reader.onloadend = () => {
                onUpdate(index, { referenceImage: reader.result as string })
            }
            reader.readAsDataURL(file)
        }
    }

    return (
        <div className="glass-card fade-in">
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
                <h2>Refinamento de Detalhes</h2>
                <span className="badge" style={{ background: 'var(--accent-color)', color: 'black' }}>
                    {details.length} Elementos
                </span>
            </div>
            <p style={{ color: 'var(--text-secondary)', marginBottom: '2rem' }}>
                Refine as descrições e anexe imagens de referência para materiais específicos.
            </p>

            {isLoading ? (
                <div style={{ textAlign: 'center', padding: '5rem' }}>
                    <Loader2 className="animate-spin" size={48} color="var(--accent-color)" />
                    <p style={{ marginTop: '1.5rem', color: 'var(--text-secondary)' }}>O Agente de Análise está mapeando seu projeto...</p>
                </div>
            ) : (
                <div className="fade-in">
                    <div style={{
                        display: 'flex',
                        flexDirection: 'column',
                        gap: '1rem',
                        marginBottom: '3rem'
                    }}>
                        {details.map((detail, index) => (
                            <div key={detail.id} className="detail-card" style={{
                                background: 'rgba(255,255,255,0.03)',
                                padding: '1.2rem',
                                borderRadius: '12px',
                                border: '1px solid var(--glass-border)',
                                display: 'flex',
                                gap: '1.5rem',
                                alignItems: 'flex-start'
                            }}>
                                {/* Left side: Image Reference */}
                                <div style={{ width: '140px', flexShrink: 0 }}>
                                    {detail.referenceImage ? (
                                        <div style={{ position: 'relative', width: '100%', aspectRatio: '1/1', borderRadius: '8px', overflow: 'hidden', border: '1px solid rgba(255,255,255,0.1)' }}>
                                            <img src={detail.referenceImage} alt="Referência" style={{ width: '100%', height: '100%', objectFit: 'cover' }} />
                                            <button
                                                onClick={() => onUpdate(index, { referenceImage: undefined })}
                                                style={{ position: 'absolute', top: '4px', right: '4px', background: 'rgba(0,0,0,0.6)', border: 'none', borderRadius: '50%', color: 'white', padding: '4px', cursor: 'pointer' }}
                                            >
                                                <X size={10} />
                                            </button>
                                        </div>
                                    ) : (
                                        <button
                                            className="btn-secondary"
                                            style={{
                                                width: '100%',
                                                aspectRatio: '1/1',
                                                fontSize: '0.7rem',
                                                padding: '0.5rem',
                                                display: 'flex',
                                                flexDirection: 'column',
                                                alignItems: 'center',
                                                justifyContent: 'center',
                                                gap: '8px',
                                                borderStyle: 'dashed',
                                                background: 'rgba(255,255,255,0.02)'
                                            }}
                                            onClick={() => {
                                                setActiveUploadIndex(index);
                                                fileInputRef.current?.click();
                                            }}
                                        >
                                            <ImageIcon size={20} style={{ opacity: 0.5 }} />
                                            <span style={{ textAlign: 'center' }}>Adicionar Referência</span>
                                        </button>
                                    )}
                                </div>

                                {/* Right side: Content */}
                                <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: '0.8rem' }}>
                                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                                        <span style={{ fontSize: '0.7rem', color: 'var(--accent-color)', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.05em' }}>
                                            Elemento #{index + 1}
                                        </span>
                                        <button
                                            onClick={() => onRemove(index)}
                                            style={{ background: 'none', border: 'none', color: 'rgba(255,75,43,0.4)', cursor: 'pointer', padding: '4px' }}
                                            title="Remover"
                                        >
                                            <Trash2 size={14} />
                                        </button>
                                    </div>

                                    <textarea
                                        value={detail.text}
                                        onChange={(e) => onUpdate(index, { text: e.target.value })}
                                        className="card-textarea"
                                        style={{
                                            background: 'rgba(255,255,255,0.02)',
                                            border: '1px solid rgba(255,255,255,0.05)',
                                            borderRadius: '8px',
                                            color: 'var(--text-primary)',
                                            fontSize: '0.95rem',
                                            lineHeight: '1.6',
                                            padding: '1rem',
                                            width: '100%',
                                            minHeight: '80px',
                                            height: 'auto',
                                            resize: 'vertical',
                                            outline: 'none',
                                            transition: 'all 0.2s ease',
                                            overflow: 'hidden' // Part of "no scroll" strategy, assuming we want it to look like a block
                                        }}
                                        onInput={(e: any) => {
                                            e.target.style.height = 'auto';
                                            e.target.style.height = e.target.scrollHeight + 'px';
                                        }}
                                        onFocus={(e) => {
                                            e.target.style.background = 'rgba(255,255,255,0.05)';
                                            e.target.style.borderColor = 'var(--accent-color)';
                                        }}
                                        onBlur={(e) => {
                                            e.target.style.background = 'rgba(255,255,255,0.02)';
                                            e.target.style.borderColor = 'rgba(255,255,255,0.05)';
                                        }}
                                        placeholder="Descreva o detalhe..."
                                        rows={2}
                                    />
                                </div>
                            </div>
                        ))}
                    </div>

                    <input
                        type="file"
                        ref={fileInputRef}
                        hidden
                        accept="image/*"
                        onChange={(e) => activeUploadIndex !== null && handleImageUpload(activeUploadIndex, e)}
                    />

                    <div style={{ display: 'flex', gap: '1rem', marginBottom: '3rem', background: 'rgba(255,255,255,0.02)', padding: '1rem', borderRadius: '12px', border: '1px dashed var(--glass-border)' }}>
                        <input
                            type="text"
                            placeholder="Adicionar novo elemento manual (Ex: Forro de gesso com sanca invertida)"
                            value={newDetail}
                            onChange={(e) => setNewDetail(e.target.value)}
                            onKeyDown={(e) => e.key === 'Enter' && handleAdd()}
                            style={{ flex: 1, background: 'none' }}
                        />
                        <button className="btn-secondary" onClick={handleAdd} style={{ whiteSpace: 'nowrap' }}>
                            <Plus size={18} /> Adicionar
                        </button>
                    </div>

                    <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '1.5rem', alignItems: 'center' }}>
                        <span style={{ fontSize: '0.8rem', color: 'var(--text-secondary)' }}>
                            Dica: Você pode editar o texto de cada card diretamente.
                        </span>
                        <button className="btn-primary" onClick={onNext}>
                            Prosseguir para Render <Check size={18} />
                        </button>
                    </div>
                </div>
            )}
        </div>
    )
}
