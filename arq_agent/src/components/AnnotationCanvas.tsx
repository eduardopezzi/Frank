import React, { useRef, useState, useEffect } from 'react'
import { Pencil, Eraser } from 'lucide-react'

interface AnnotationCanvasProps {
    imageUrl: string;
    onSaveState?: (imageData: string) => void;
}

export const AnnotationCanvas: React.FC<AnnotationCanvasProps> = ({ imageUrl, onSaveState }) => {
    const canvasRef = useRef<HTMLCanvasElement>(null)
    const [isDrawing, setIsDrawing] = useState(false)
    const [mode, setMode] = useState<'draw' | 'erase'>('draw')

    useEffect(() => {
        const canvas = canvasRef.current
        if (!canvas) return
        const ctx = canvas.getContext('2d')
        if (!ctx) return

        const img = new Image()
        img.crossOrigin = "anonymous"
        img.src = imageUrl
        img.onload = () => {
            canvas.width = img.width
            canvas.height = img.height
            ctx.drawImage(img, 0, 0)
        }
    }, [imageUrl])

    const startDrawing = (e: React.MouseEvent) => {
        const canvas = canvasRef.current
        if (!canvas) return
        const ctx = canvas.getContext('2d')
        if (!ctx) return

        setIsDrawing(true)
        const rect = canvas.getBoundingClientRect()
        const scaleX = canvas.width / rect.width
        const scaleY = canvas.height / rect.height

        ctx.beginPath()
        ctx.moveTo((e.clientX - rect.left) * scaleX, (e.clientY - rect.top) * scaleY)
    }

    const draw = (e: React.MouseEvent) => {
        if (!isDrawing) return
        const canvas = canvasRef.current
        const ctx = canvas?.getContext('2d')
        if (!canvas || !ctx) return

        const rect = canvas.getBoundingClientRect()
        const scaleX = canvas.width / rect.width
        const scaleY = canvas.height / rect.height

        ctx.lineWidth = 5
        ctx.lineCap = 'round'

        if (mode === 'draw') {
            ctx.globalCompositeOperation = 'source-over'
            ctx.strokeStyle = '#ff4b2b'
        } else {
            // For erasing, we'd need to re-draw the image underneath or just draw over with a specific color.
            // Simplest is to just draw red circles for now as requested "marcar na imagem".
            ctx.globalCompositeOperation = 'destination-out'
            ctx.lineWidth = 20
        }

        ctx.lineTo((e.clientX - rect.left) * scaleX, (e.clientY - rect.top) * scaleY)
        ctx.stroke()
    }

    const stopDrawing = () => {
        setIsDrawing(false)
        if (onSaveState && canvasRef.current) {
            onSaveState(canvasRef.current.toDataURL())
        }
    }

    const reset = () => {
        const canvas = canvasRef.current
        if (!canvas) return
        const ctx = canvas.getContext('2d')
        if (!ctx) return
        const img = new Image()
        img.src = imageUrl
        img.onload = () => ctx.drawImage(img, 0, 0)
    }

    return (
        <div style={{ position: 'relative', overflow: 'hidden', borderRadius: '8px' }}>
            <div style={{
                position: 'absolute', top: '10px', left: '10px', zIndex: 10,
                display: 'flex', gap: '0.5rem', background: 'rgba(0,0,0,0.6)',
                padding: '5px', borderRadius: '8px', backdropFilter: 'blur(5px)'
            }}>
                <button
                    className={mode === 'draw' ? 'btn-primary' : 'btn-secondary'}
                    style={{ padding: '8px' }}
                    onClick={() => setMode('draw')}
                >
                    <Pencil size={18} />
                </button>
                <button
                    className={mode === 'erase' ? 'btn-primary' : 'btn-secondary'}
                    style={{ padding: '8px' }}
                    onClick={() => setMode('erase')}
                >
                    <Eraser size={18} />
                </button>
                <button className="btn-secondary" style={{ padding: '8px' }} onClick={reset}>
                    Reset
                </button>
            </div>

            <canvas
                ref={canvasRef}
                onMouseDown={startDrawing}
                onMouseMove={draw}
                onMouseUp={stopDrawing}
                onMouseLeave={stopDrawing}
                style={{ width: '100%', cursor: mode === 'draw' ? 'crosshair' : 'default', display: 'block' }}
            />
        </div>
    )
}
