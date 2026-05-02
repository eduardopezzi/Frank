import { useEffect, useState, useMemo } from 'react';
import EquipmentTimeline from './EquipmentTimeline';
import { ErrorBoundary } from './ErrorBoundary';

/**
 * Componente wrapper que conecta os dados filtrados ao EquipmentTimeline.
 */
const InteractiveGanttChart = ({ tasks, onSave, onSimulationCreate }) => {
  return (
    <div className="flex flex-col h-full" style={{ minHeight: '500px' }}>
      <ErrorBoundary>
        <EquipmentTimeline
          tasks={tasks}
          onSave={onSave}
        />
      </ErrorBoundary>
    </div>
  );
};

export default InteractiveGanttChart;