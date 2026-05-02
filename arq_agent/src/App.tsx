import { useState } from 'react'
import { Upload, Settings, List, Image as ImageIcon, CheckCircle } from 'lucide-react'
import './App.css'
import { UploadStep } from './components/UploadStep'
import { DetailReviewStep } from './components/DetailReviewStep'
import { RenderStep } from './components/RenderStep'
import { ComparisonStep } from './components/ComparisonStep'
import { analyzeSketch, type Detail } from './services/gemini'

type Step = 'setup' | 'analysis' | 'review_details' | 'render' | 'comparison' | 'success'

function App() {
  const [currentStep, setCurrentStep] = useState<Step>('setup')
  const [isLoading, setIsLoading] = useState(false)
  const [projectData, setProjectData] = useState({
    style: 'Moderno Minimalista',
    lighting: 'Luz Natural (Golden Hour)',
    theme: 'Residencial de Luxo',
    sketchImage: null as string | null,
    details: [] as Detail[],
    renderedImage: null as string | null,
    refinementAnnotation: undefined as string | undefined,
    refinementFeedback: undefined as string | undefined,
  })

  const steps: { key: Step; label: string; icon: any }[] = [
    { key: 'setup', label: 'Setup', icon: Settings },
    { key: 'analysis', label: 'Upload', icon: Upload },
    { key: 'review_details', label: 'Detalhes', icon: List },
    { key: 'render', label: 'Renderização', icon: ImageIcon },
    { key: 'comparison', label: 'Revisão', icon: CheckCircle },
  ]

  const handleNext = async () => {
    if (currentStep === 'setup') setCurrentStep('analysis')
    else if (currentStep === 'analysis') {
      if (projectData.sketchImage) {
        setCurrentStep('review_details')
        setIsLoading(true)
        try {
          const result = await analyzeSketch(projectData.sketchImage)
          const newDetails: Detail[] = result.elements.map((text: string) => ({
            id: Math.random().toString(36).substr(2, 9),
            text
          }))
          setProjectData(prev => ({ ...prev, details: newDetails }))
        } catch (error: any) {
          console.error(error)
          const msg = error?.message ?? "Erro desconhecido"
          alert(`Erro ao analisar imagem:\n${msg}`)
        } finally {
          setIsLoading(false)
        }
      }
    }
    else if (currentStep === 'review_details') setCurrentStep('render')
    else if (currentStep === 'render') setCurrentStep('comparison')
    else if (currentStep === 'comparison') setCurrentStep('success')
  }

  const handleBack = () => {
    if (currentStep === 'analysis') setCurrentStep('setup')
    else if (currentStep === 'review_details') setCurrentStep('analysis')
    else if (currentStep === 'render') setCurrentStep('review_details')
    else if (currentStep === 'comparison') setCurrentStep('render')
  }

  const handleRefine = async (annotatedImage: string, feedback: string) => {
    if (!projectData.sketchImage) return
    setCurrentStep('render')
    setProjectData(prev => ({
      ...prev,
      refinementAnnotation: annotatedImage,
      refinementFeedback: feedback,
    } as any))
  }

  const handleDownload = () => {
    if (!projectData.renderedImage) return
    const link = document.createElement('a')
    link.href = projectData.renderedImage
    link.download = `ArqAgent-Render-${Date.now()}.png`
    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)
  }

  return (
    <div className="container">
      <header style={{ textAlign: 'center', marginBottom: '4rem' }}>
        <h1 style={{ fontSize: '3rem', color: 'var(--accent-color)' }}>ArqAgent</h1>
        <p style={{ color: 'var(--text-secondary)' }}>IA para Renderização Arquitetônica de Alta Performance</p>
      </header>

      {currentStep !== 'success' && (
        <nav className="step-indicator">
          {steps.map((s, i) => (
            <div key={s.key} className={`step ${currentStep === s.key ? 'active' : ''}`}>
              <div className="step-circle">{i + 1}</div>
              <span style={{ fontSize: '0.8rem', fontWeight: 600 }}>{s.label}</span>
            </div>
          ))}
        </nav>
      )}

      <main className="fade-in">
        {currentStep === 'setup' && (
          <div className="glass-card">
            <h2>Configurações do Projeto</h2>
            <p style={{ color: 'var(--text-secondary)', marginBottom: '2rem' }}>Defina o estilo e a atmosfera do ambiente.</p>

            <div className="grid grid-2">
              <div>
                <label>Estilo do Ambiente</label>
                <select
                  value={projectData.style}
                  onChange={(e) => setProjectData({ ...projectData, style: e.target.value })}
                >
                  <option>Moderno Minimalista</option>
                  <option>Industrial</option>
                  <option>Escandinavo</option>
                  <option>Clássico Contemporâneo</option>
                  <option>Biofílico</option>
                </select>

                <label>Tema do Projeto</label>
                <select
                  value={projectData.theme}
                  onChange={(e) => setProjectData({ ...projectData, theme: e.target.value })}
                >
                  <option>Residencial de Alto Padrão</option>
                  <option>Corporativo Moderno</option>
                  <option>Varejo / Comercial</option>
                  <option>Hotelaria e Lazer</option>
                </select>
              </div>

              <div>
                <label>Iluminação</label>
                <select
                  value={projectData.lighting}
                  onChange={(e) => setProjectData({ ...projectData, lighting: e.target.value })}
                >
                  <option>Luz Natural (Golden Hour)</option>
                  <option>Meio-dia (Luz Clara)</option>
                  <option>Noturna (Artificial Focalizada)</option>
                  <option>Nublado (Luz Suave)</option>
                </select>

                <label>Estilo de Desenho</label>
                <input type="text" placeholder="Ex: Fotorrealista, Sketch Artístico, Maquete Eletrônica..." />
              </div>
            </div>

            <div style={{ marginTop: '2rem', display: 'flex', justifyContent: 'flex-end' }}>
              <button className="btn-primary" onClick={handleNext}>
                Prosseguir para Upload <Upload size={18} />
              </button>
            </div>
          </div>
        )}

        {currentStep === 'analysis' && (
          <UploadStep
            onImageSelected={(base64) => setProjectData({ ...projectData, sketchImage: base64 })}
            onNext={handleNext}
          />
        )}

        {currentStep === 'review_details' && (
          <DetailReviewStep
            details={projectData.details}
            isLoading={isLoading}
            onUpdate={(index, updated) => {
              const newDetails = [...projectData.details]
              newDetails[index] = { ...newDetails[index], ...updated }
              setProjectData(prev => ({ ...prev, details: newDetails }))
            }}
            onAdd={(text) => setProjectData(prev => ({
              ...prev,
              details: [...prev.details, { id: Math.random().toString(36).substr(2, 9), text }]
            }))}
            onRemove={(index) => setProjectData(prev => ({
              ...prev,
              details: prev.details.filter((_, i) => i !== index)
            }))}
            onNext={handleNext}
          />
        )}

        {currentStep === 'render' && (
          <RenderStep
            context={projectData as any}
            onRenderComplete={(url) => {
              setProjectData(prev => ({ ...prev, renderedImage: url }))
              setCurrentStep('comparison')
            }}
            onBack={handleBack}
          />
        )}

        {currentStep === 'comparison' && projectData.sketchImage && projectData.renderedImage && (
          <ComparisonStep
            originalImage={projectData.sketchImage}
            renderedImage={projectData.renderedImage}
            onRefine={handleRefine}
            onApprove={handleNext}
          />
        )}

        {currentStep === 'success' && (
          <div className="glass-card" style={{ textAlign: 'center', padding: '5rem' }}>
            <CheckCircle size={80} color="var(--accent-color)" style={{ marginBottom: '2rem' }} />
            <h2 style={{ fontSize: '2.5rem' }}>Projeto Finalizado!</h2>
            <p style={{ color: 'var(--text-secondary)', marginBottom: '3rem' }}>
              Sua renderização fotorrealista foi concluída com sucesso e os arquivos de alta resolução estão prontos.
            </p>
            <div style={{ display: 'flex', justifyContent: 'center', gap: '1.5rem' }}>
              <button className="btn-primary" onClick={handleDownload}>Baixar Arquivo Final</button>
              <button className="btn-secondary" onClick={() => setCurrentStep('setup')}>Novo Projeto</button>
            </div>
          </div>
        )}
      </main>
    </div>
  )
}

export default App
