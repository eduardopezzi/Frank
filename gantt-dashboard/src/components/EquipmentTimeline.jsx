import { useState, useMemo, useRef, useEffect, useCallback } from 'react';
import { format, addDays, startOfDay, differenceInMilliseconds } from 'date-fns';
import { ptBR } from 'date-fns/locale';
import { ZoomIn, ZoomOut, Save, Play, RefreshCw } from 'lucide-react';

// ── Cores por ordem de produção ──────────────────────────────────────────────
const ORDER_COLORS = [
    '#2563eb', '#dc2626', '#16a34a', '#d97706', '#7c3aed',
    '#db2777', '#0891b2', '#4f46e5', '#ea580c', '#059669',
    '#9333ea', '#e11d48',
];

const getColorForOrder = (orderId) => {
    if (!orderId) return '#94a3b8';
    let hash = 0;
    const str = String(orderId);
    for (let i = 0; i < str.length; i++) hash = str.charCodeAt(i) + ((hash << 5) - hash);
    return ORDER_COLORS[Math.abs(hash) % ORDER_COLORS.length];
};

// ── Zoom levels ──────────────────────────────────────────────────────────────
const ZOOM_LEVELS = [
    { label: '1/4 Dia', pxPerHour: 120, scaleUnit: 'hour', scaleStep: 6, headerUnit: 'day' },
    { label: '1/2 Dia', pxPerHour: 60, scaleUnit: 'hour', scaleStep: 12, headerUnit: 'day' },
    { label: 'Dia', pxPerHour: 30, scaleUnit: 'day', scaleStep: 1, headerUnit: 'month' },
    { label: 'Semana', pxPerHour: 4, scaleUnit: 'day', scaleStep: 7, headerUnit: 'month' },
    { label: 'Mês', pxPerHour: 1.2, scaleUnit: 'day', scaleStep: 30, headerUnit: 'year' },
];

const ROW_HEIGHT = 44;

// ── Tooltip Component ────────────────────────────────────────────────────────
const Tooltip = ({ task, x, y }) => {
    if (!task) return null;
    return (
        <div
            style={{
                position: 'fixed',
                left: x + 16, top: y + 16,
                zIndex: 99999,
                pointerEvents: 'none',
                backgroundColor: 'rgba(15, 23, 42, 0.96)',
                backdropFilter: 'blur(8px)',
            }}
            className="text-white text-xs rounded-lg p-3 shadow-2xl whitespace-nowrap border border-gray-700"
        >
            <div className="font-bold mb-1 text-sm">Ordem: {task.order}</div>
            <div><strong>Equipamento:</strong> {task.equipment}</div>
            <div><strong>Produto:</strong> {task.product}</div>
            <div><strong>Operação:</strong> {task.operation}</div>
            <div className="mt-2 pt-2 border-t border-gray-700">
                <div><strong>Início:</strong> {format(new Date(task.start), 'dd/MM/yyyy HH:mm', { locale: ptBR })}</div>
                <div><strong>Fim:</strong> {format(new Date(task.end), 'dd/MM/yyyy HH:mm', { locale: ptBR })}</div>
                <div className="mt-1 text-gray-400">
                    <div><strong>Setup:</strong> {Math.round(task.setuptime / 60000)} min</div>
                    <div><strong>Lead Time:</strong> {Math.round(task.leadtime / 60000)} min</div>
                </div>
            </div>
        </div>
    );
};

// ── Main Component ───────────────────────────────────────────────────────────
const EquipmentTimeline = ({ tasks = [], onSave }) => {
    const [zoomIndex, setZoomIndex] = useState(2); // "Dia"
    const [tooltip, setTooltip] = useState(null);
    const [hoveredOrder, setHoveredOrder] = useState(null);
    const scrollRef = useRef(null);

    const zoom = ZOOM_LEVELS[zoomIndex];

    // ── Group tasks by equipment ─────────────────────────────────────────────
    const { equipments, tasksByEquipment } = useMemo(() => {
        const map = {};
        (tasks || []).forEach(t => {
            if (t.start === null || t.end === null) return;
            const eq = String(t.equipment || 'S/E');
            if (!map[eq]) map[eq] = [];
            map[eq].push(t);
        });
        const sorted = Object.keys(map).sort((a, b) => a.localeCompare(b, undefined, { numeric: true }));
        return { equipments: sorted, tasksByEquipment: map };
    }, [tasks]);

    // ── Compute time range ───────────────────────────────────────────────────
    const { minTime, maxTime, totalMs, totalWidth, timeMarkers } = useMemo(() => {
        const validTasks = tasks.filter(t => t.start !== null && t.end !== null);
        if (validTasks.length === 0) {
            const now = Date.now();
            return { minTime: now, maxTime: now + 86400000, totalMs: 86400000, totalWidth: 24 * zoom.pxPerHour, timeMarkers: [] };
        }

        const min = Math.min(...validTasks.map(t => t.start));
        const max = Math.max(...validTasks.map(t => t.end));
        const margin = 12 * 3600000; // 12h buffer
        const finalMin = min - margin;
        const finalMax = max + margin;
        const total = finalMax - finalMin;
        const width = (total / 3600000) * zoom.pxPerHour;

        // Generate time markers
        const markers = [];
        const stepMs = zoom.scaleUnit === 'hour'
            ? zoom.scaleStep * 3600000
            : zoom.scaleStep * 86400000;

        const start = startOfDay(new Date(finalMin)).getTime();
        for (let t = start; t <= finalMax; t += stepMs) {
            if (t >= finalMin) {
                markers.push(t);
            }
        }

        return { minTime: finalMin, maxTime: finalMax, totalMs: total, totalWidth: width, timeMarkers: markers };
    }, [tasks, zoom]);

    // ── Position helpers ─────────────────────────────────────────────────────
    const getLeft = useCallback((timestamp) => {
        return ((timestamp - minTime) / totalMs) * totalWidth;
    }, [minTime, totalMs, totalWidth]);

    const getWidth = useCallback((start, end) => {
        return Math.max(4, ((end - start) / totalMs) * totalWidth);
    }, [totalMs, totalWidth]);

    // ── Format marker labels ─────────────────────────────────────────────────
    const formatMarker = useCallback((timestamp) => {
        const d = new Date(timestamp);
        if (zoom.scaleUnit === 'hour') {
            return format(d, 'dd/MM HH:mm', { locale: ptBR });
        }
        if (zoom.scaleStep >= 7) {
            return format(d, 'dd MMM', { locale: ptBR });
        }
        return format(d, 'dd/MM', { locale: ptBR });
    }, [zoom]);

    // ── Zoom handlers ────────────────────────────────────────────────────────
    const handleZoomIn = () => setZoomIndex(i => Math.max(0, i - 1));
    const handleZoomOut = () => setZoomIndex(i => Math.min(ZOOM_LEVELS.length - 1, i + 1));

    // ── Empty state ──────────────────────────────────────────────────────────
    if (equipments.length === 0) {
        return (
            <div className="bg-white rounded-lg shadow-md p-8 text-center">
                <div className="text-gray-400 text-lg mb-2">Nenhuma tarefa encontrada</div>
                <div className="text-gray-500 text-sm">Selecione um snapshot e ajuste os filtros</div>
            </div>
        );
    }

    return (
        <div className="flex flex-col h-full bg-white rounded-lg shadow-md overflow-hidden">
            {/* ── Toolbar ─────────────────────────────────────────────────────── */}
            <div className="flex items-center gap-3 px-4 py-3 bg-gray-50 border-b border-gray-200 flex-shrink-0">
                <button onClick={handleZoomIn} className="p-2 rounded hover:bg-gray-200 transition-colors" title="Zoom In">
                    <ZoomIn size={18} className="text-gray-700" />
                </button>
                <span className="text-sm font-medium text-gray-700 min-w-[60px] text-center">{zoom.label}</span>
                <button onClick={handleZoomOut} className="p-2 rounded hover:bg-gray-200 transition-colors" title="Zoom Out">
                    <ZoomOut size={18} className="text-gray-700" />
                </button>
                <div className="border-l border-gray-300 h-6 mx-2" />
                <button onClick={() => onSave && onSave(tasks)} className="flex items-center gap-2 px-4 py-2 rounded bg-blue-600 hover:bg-blue-700 text-white text-sm font-medium transition-colors">
                    <Save size={16} /> Salvar
                </button>
                <div className="ml-auto text-sm text-gray-500">
                    {equipments.length} equipamentos · {tasks.filter(t => t.start !== null).length} ordens
                </div>
            </div>

            {/* ── Chart Area ──────────────────────────────────────────────────── */}
            <div className="flex flex-1 overflow-hidden min-h-0">
                {/* Equipment column (sticky left) */}
                <div className="flex-shrink-0 w-[140px] border-r border-gray-200 bg-gray-50 overflow-hidden z-10">
                    {/* Header spacer */}
                    <div className="h-[50px] border-b border-gray-200 flex items-center px-3">
                        <span className="text-xs font-semibold text-gray-600 uppercase tracking-wider">Equipamento</span>
                    </div>
                    {/* Equipment labels */}
                    <div className="overflow-y-hidden" id="eq-labels">
                        {equipments.map(eq => (
                            <div
                                key={eq}
                                style={{ height: ROW_HEIGHT }}
                                className="flex items-center px-3 border-b border-gray-100 text-sm font-medium text-gray-800"
                            >
                                {eq}
                            </div>
                        ))}
                    </div>
                </div>

                {/* Timeline area (scrollable) */}
                <div className="flex-1 overflow-auto" ref={scrollRef}
                    onScroll={(e) => {
                        // Sync vertical scroll of equipment labels
                        const labelsEl = document.getElementById('eq-labels');
                        if (labelsEl) labelsEl.scrollTop = e.target.scrollTop;
                    }}
                >
                    <div style={{ width: totalWidth, minHeight: '100%' }}>
                        {/* Time header */}
                        <div className="sticky top-0 z-20 bg-gray-50 border-b border-gray-200 h-[50px] relative">
                            {timeMarkers.map((t, i) => (
                                <div
                                    key={i}
                                    className="absolute top-0 bottom-0 border-l border-gray-300"
                                    style={{ left: getLeft(t) }}
                                >
                                    <span className="text-[10px] text-gray-500 whitespace-nowrap pl-1 pt-1 block">{formatMarker(t)}</span>
                                </div>
                            ))}
                        </div>

                        {/* Rows */}
                        {equipments.map(eq => (
                            <div
                                key={eq}
                                className="relative border-b border-gray-100"
                                style={{ height: ROW_HEIGHT }}
                            >
                                {/* Grid lines */}
                                {timeMarkers.map((t, i) => (
                                    <div
                                        key={i}
                                        className="absolute top-0 bottom-0 border-l border-gray-50"
                                        style={{ left: getLeft(t) }}
                                    />
                                ))}

                                {/* Task bars */}
                                {(tasksByEquipment[eq] || []).map(task => {
                                    const left = getLeft(task.start);
                                    const w = getWidth(task.start, task.end);
                                    const color = getColorForOrder(task.order);
                                    const isDimmed = hoveredOrder && task.order !== hoveredOrder;
                                    const isHighlighted = hoveredOrder && task.order === hoveredOrder;

                                    return (
                                        <div
                                            key={`${task.order}-${task.workflow}`}
                                            className={`absolute rounded cursor-pointer transition-all duration-150 ${isHighlighted ? 'ring-2 ring-white shadow-lg scale-y-110 z-10' : ''}`}
                                            style={{
                                                left, width: w,
                                                top: 6, bottom: 6,
                                                backgroundColor: color,
                                                opacity: isDimmed ? 0.3 : 0.92,
                                                border: '1px solid rgba(0,0,0,0.15)',
                                            }}
                                            onMouseEnter={(e) => {
                                                setHoveredOrder(task.order);
                                                setTooltip({ task, x: e.clientX, y: e.clientY });
                                            }}
                                            onMouseMove={(e) => {
                                                setTooltip(prev => prev ? { ...prev, x: e.clientX, y: e.clientY } : null);
                                            }}
                                            onMouseLeave={() => {
                                                setHoveredOrder(null);
                                                setTooltip(null);
                                            }}
                                        >
                                            {w > 60 && (
                                                <span className="text-[10px] text-white font-medium truncate block px-1 leading-[calc(var(--row))] pt-[3px]">
                                                    {task.order}
                                                </span>
                                            )}
                                        </div>
                                    );
                                })}
                            </div>
                        ))}
                    </div>
                </div>
            </div>

            {/* ── Footer ──────────────────────────────────────────────────────── */}
            <div className="flex items-center gap-6 px-4 py-2 bg-gray-50 border-t border-gray-200 text-xs text-gray-500 flex-shrink-0">
                <div className="flex items-center gap-2">
                    <div className="w-3 h-3 rounded" style={{ background: 'linear-gradient(90deg, #2563eb, #16a34a, #d97706, #dc2626)' }} />
                    <span>Cores por Ordem de Produção</span>
                </div>
                <span>Passe o mouse sobre uma barra para ver detalhes</span>
            </div>

            {/* Tooltip portal */}
            {tooltip && <Tooltip task={tooltip.task} x={tooltip.x} y={tooltip.y} />}
        </div>
    );
};

export default EquipmentTimeline;
