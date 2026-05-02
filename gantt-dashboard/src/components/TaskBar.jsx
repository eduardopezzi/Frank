import { useState } from 'react';
import { format } from 'date-fns';
import { ptBR } from 'date-fns/locale';

// Função para gerar cor consistente e vibrante baseada na ordem de produção
const getColorFromOrder = (order) => {
  if (!order) return '#94a3b8'; // Cinza para ordem null

  // Utiliza um formato de hash customizado para distribuir melhor as cores
  const str = String(order);
  let hash = 0;
  for (let i = 0; i < str.length; i++) {
    hash = str.charCodeAt(i) + ((hash << 5) - hash);
  }

  // Array de cores profissionais e vibrantes para distinguir ordens de produção
  const colors = [
    '#3b82f6', // blue-500
    '#ef4444', // red-500
    '#10b981', // emerald-500
    '#f59e0b', // amber-500
    '#8b5cf6', // violet-500
    '#ec4899', // pink-500
    '#06b6d4', // cyan-500
    '#eab308', // yellow-500
    '#6366f1', // indigo-500
    '#f97316', // orange-500
    '#14b8a6', // teal-500
    '#d946ef', // fuchsia-500
  ];

  const index = Math.abs(hash) % colors.length;
  return colors[index];
};

const TaskBar = ({ task, left, width, hoveredOrder, onHover }) => {
  const [showTooltip, setShowTooltip] = useState(false);
  const color = getColorFromOrder(task.order);

  // Se existe uma ordem de produção hoverada, e ela não é esta, diminuir a opacidade.
  // Caso contrário fica 100%.
  const isDimmed = hoveredOrder && task.order !== hoveredOrder;
  const isHighlighted = hoveredOrder && task.order === hoveredOrder;

  return (
    <div
      className={`absolute top-2 bottom-2 rounded cursor-pointer transition-all duration-200 flex items-center px-2 shadow-sm ${isHighlighted ? 'ring-2 ring-black scale-[1.02] z-10' : ''
        }`}
      style={{
        left: `${left}%`,
        width: `${width}%`,
        minWidth: '12px',
        backgroundColor: color,
        opacity: isDimmed ? 0.3 : 0.95,
      }}
      onMouseEnter={() => {
        setShowTooltip(true);
        if (onHover && task.order) onHover(task.order);
      }}
      onMouseLeave={() => {
        setShowTooltip(false);
        if (onHover) onHover(null);
      }}
    >
      {width > 3 && (
        <span className="text-xs text-white font-medium truncate">
          {task.workflow}
        </span>
      )}

      {showTooltip && (
        <div className="absolute z-50 bg-gray-900 text-white text-xs rounded-lg p-3 shadow-xl pointer-events-none whitespace-nowrap top-full mt-2">
          <div className="font-bold mb-1 text-sm">
            Workflow: {task.workflow}
          </div>
          <div><strong>Ordem:</strong> {task.order}</div>
          <div><strong>Tipo:</strong> {task.type}</div>
          <div><strong>Equipamento:</strong> {task.equipment}</div>
          <div><strong>Produto:</strong> {task.product}</div>
          <div><strong>Operação:</strong> {task.operation}</div>
          <div className="mt-2 pt-2 border-t border-gray-700">
            <div><strong>Prazo (Deadline):</strong> {format(new Date(task.deadline), "dd/MM/yyyy HH:mm", { locale: ptBR })}</div>
            <div className="mt-1"><strong>Início:</strong> {format(new Date(task.start), "dd/MM/yyyy HH:mm", { locale: ptBR })}</div>
            <div><strong>Fim:</strong> {format(new Date(task.end), "dd/MM/yyyy HH:mm", { locale: ptBR })}</div>
            <div className="mt-1 text-gray-400">
              <div><strong>Setup:</strong> {Math.round(task.setuptime / 60000)} min</div>
              <div><strong>Lead Time:</strong> {Math.round(task.leadtime / 60000)} min</div>
              {task.end - (task.start + task.leadtime + task.setuptime) > 60000 && (
                <div className="text-yellow-400">
                  <strong>Interrupções:</strong> {Math.round((task.end - (task.start + task.leadtime + task.setuptime)) / 3600000)}h {Math.round(((task.end - (task.start + task.leadtime + task.setuptime)) % 3600000) / 60000)}min
                </div>
              )}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default TaskBar;