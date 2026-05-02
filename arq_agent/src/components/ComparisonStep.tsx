import React, { useState } from 'react'
import { AnnotationCanvas } from './AnnotationCanvas'
import { RefreshCw, CheckCircle, MessageSquare } from 'lucide-react'

interface ComparisonStepProps {
    originalImage: string;
    renderedImage: string;
    onRefine: (annotations: string, feedback: string) => void;
    onApprove: () => void;
}

export const ComparisonStep: React.FC<ComparisonStepProps> = ({
    originalImage, renderedImage, onRefine, onApprove
}) => {
    const [feedback, setFeedback] = useState('')
    const [annotatedImage, setAnnotatedImage] = useState('')

    return (
        <div className="glass-card fade-in">
            <h2>Revisão e Comparação</h2>
            <p style={{ color: 'var(--text-secondary)', marginBottom: '2rem' }}>
                Compare o sketch 3D original com a renderização gerada. Marque os ajustes necessários na imagem.
            </p>

            <div className="grid grid-2">
                <div>
                    <label>Sketch Original</label>
                    <img
                        src={originalImage}
                        alt="Original Sketch"
                        style={{ width: '100%', borderRadius: '8px', border: '1px solid var(--glass-border)' }}
                    />
                </div>
                <div>
                    <label>Renderização (Marque aqui o que deseja mudar)</label>
                    <AnnotationCanvas
                        imageUrl={renderedImage}
                        onSaveState={setAnnotatedImage}
                    />
                </div>
            </div>

            <div style={{ marginTop: '2rem' }}>
                <label style={{ display: 'flex', alignItems: 'center', gap: '5px' }}>
                    <MessageSquare size={16} /> Detalhes Adicionais de Ajuste
                </label>
                <textarea
                    placeholder="Descreva o que não gostou ou o que precisa ser melhorado (ex: a luz está muito amarela, o mármore precisa de mais brilho...)"
                    rows={4}
                    value={feedback}
                    onChange={(e) => setFeedback(e.target.value)}
                />
            </div>

            <div style={{ marginTop: '2rem', display: 'flex', justifyContent: 'flex-end', gap: '1rem' }}>
                <button
                    className="btn-secondary"
                    onClick={() => onRefine(annotatedImage, feedback)}
                    style={{ display: 'flex', alignItems: 'center', gap: '8px' }}
                >
                    Solicitar Melhorias <RefreshCw size={18} />
                </button>
                <button
                    className="btn-primary"
                    onClick={onApprove}
                >
                    Aprovar Render <CheckCircle size={18} />
                </button>
            </div>
        </div>
    )
}
