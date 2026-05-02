import React, { useState, useEffect } from 'react'
import { Sparkles, AlertCircle } from 'lucide-react'
import { generateRenderSpec, renderImage, refineRender, type Detail } from '../services/gemini'

interface RenderStepProps {
    context: {
        style: string;
        lighting: string;
        theme: string;
        details: Detail[];
        sketchImage: string | null;
        refinementAnnotation?: string;
        refinementFeedback?: string;
    };
    onRenderComplete: (imageUrl: string) => void;
    onBack: () => void;
}

const STAGES = [
    { label: "Gerando especificação técnica (Agente 2)...", progress: 20 },
    { label: "Montando prompt de renderização...", progress: 40 },
    { label: "Enviando para o Nano Banana (Agente 3)...", progress: 60 },
    { label: "Processando texturas e materiais...", progress: 80 },
    { label: "Aplicando iluminação e pós-processamento...", progress: 95 },
]

export const RenderStep: React.FC<RenderStepProps> = ({
    context, onRenderComplete, onBack
}) => {
    const [progress, setProgress] = useState(0)
    const [stageLabel, setStageLabel] = useState("Iniciando renderização...")
    const [error, setError] = useState<string | null>(null)
    const [specJson, setSpecJson] = useState<string | null>(null)

    useEffect(() => {
        let cancelled = false
        const isRefinement = !!(context.refinementAnnotation && context.refinementFeedback)

        const run = async () => {
            try {
                if (isRefinement) {
                    setStageLabel("Analisando anotações do arquiteto (Agente 5)...")
                    setProgress(30)

                    const imageUrl = await refineRender(
                        context.refinementAnnotation!,
                        context.sketchImage!,
                        context.refinementFeedback!,
                        context.details,
                        context
                    )

                    if (cancelled) return
                    setProgress(100)
                    setStageLabel("Imagem refinada com sucesso!")
                    setTimeout(() => { if (!cancelled) onRenderComplete(imageUrl) }, 800)
                } else {
                    setStageLabel(STAGES[0].label)
                    setProgress(STAGES[0].progress)

                    const { prompt: renderPrompt, specJson: spec } = await generateRenderSpec(
                        context.details,
                        context
                    )

                    if (cancelled) return
                    setSpecJson(spec)
                    setStageLabel(STAGES[1].label)
                    setProgress(STAGES[1].progress)

                    setStageLabel(STAGES[2].label)
                    setProgress(STAGES[2].progress)

                    const imageUrl = await renderImage(
                        renderPrompt,
                        context.sketchImage!,
                        context
                    )

                    if (cancelled) return
                    setProgress(100)
                    setStageLabel(STAGES[4].label)
                    setTimeout(() => { if (!cancelled) onRenderComplete(imageUrl) }, 800)
                }
            } catch (err: any) {
                if (!cancelled) {
                    setError(err.message ?? "Erro desconhecido na renderização.")
                }
            }
        }

        run()
        return () => { cancelled = true }
    }, [])

    return (
        <div className="glass-card fade-in" style={{ textAlign: 'center' }}>
            <h2>{context.refinementAnnotation ? 'Refinando Renderização' : 'Gerando Renderização'}</h2>
            <p style={{ color: 'var(--text-secondary)', marginBottom: '3rem' }}>
                {context.refinementAnnotation
                    ? 'Aplicando as correções solicitadas com base nas anotações do arquiteto...'
                    : 'O Nano Banana está aplicando materiais e iluminação com base nas especificações...'}
            </p>

            {error ? (
                <div style={{
                    padding: '2rem', background: 'rgba(255,75,43,0.1)',
                    borderRadius: '12px', border: '1px solid rgba(255,75,43,0.3)',
                    maxWidth: '600px', margin: '0 auto'
                }}>
                    <AlertCircle size={40} color="#ff4b2b" style={{ marginBottom: '1rem' }} />
                    <h3 style={{ color: '#ff4b2b' }}>Erro na Renderização</h3>
                    <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem' }}>{error}</p>
                    <button className="btn-secondary" style={{ marginTop: '1.5rem' }} onClick={onBack}>
                        Voltar e Tentar Novamente
                    </button>
                </div>
            ) : (
                <div style={{ maxWidth: '600px', margin: '0 auto' }}>
                    <div style={{
                        height: '8px', background: 'rgba(255,255,255,0.05)',
                        borderRadius: '4px', overflow: 'hidden', marginBottom: '1rem'
                    }}>
                        <div style={{
                            height: '100%', width: `${progress}%`, background: 'var(--accent-color)',
                            transition: 'width 0.6s ease', boxShadow: '0 0 12px var(--accent-color)'
                        }} />
                    </div>

                    <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.8rem', color: 'var(--text-secondary)', marginBottom: '3rem' }}>
                        <span>{stageLabel}</span>
                        <span>{progress}%</span>
                    </div>

                    {specJson && (
                        <div style={{
                            textAlign: 'left', padding: '1rem', background: 'rgba(0,0,0,0.3)',
                            borderRadius: '8px', border: '1px solid var(--glass-border)',
                            marginBottom: '2rem', maxHeight: '150px', overflow: 'auto'
                        }}>
                            <p style={{ fontSize: '0.7rem', color: 'var(--text-secondary)', marginBottom: '0.5rem' }}>ESPECIFICAÇÃO TÉCNICA (Agente 2)</p>
                            <pre style={{ fontSize: '0.7rem', color: '#7ec8a4', margin: 0 }}>{specJson}</pre>
                        </div>
                    )}

                    <div style={{ padding: '2rem', background: 'rgba(0,0,0,0.2)', borderRadius: '12px', border: '1px solid var(--glass-border)' }}>
                        <Sparkles size={48} color="var(--accent-color)" style={{ marginBottom: '1rem' }} />
                        <h3>Inteligência Artificial Ativa</h3>
                        <p style={{ fontSize: '0.9rem', color: 'var(--text-secondary)' }}>
                            Estilo: {context.style} | Luz: {context.lighting}
                        </p>
                        <p style={{ fontSize: '0.8rem', color: 'var(--text-secondary)', marginTop: '0.5rem' }}>
                            {context.details.length} elementos mapeados para renderização fiel ao 3D
                        </p>
                    </div>
                </div>
            )}
        </div>
    )
}
