import { useState, useMemo, useEffect } from 'react';
import FilterPanel from './components/FilterPanel';
import InteractiveGanttChart from './components/InteractiveGanttChart';
import SnapshotSelector from './components/SnapshotSelector';
import { BarChart3 } from 'lucide-react';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || `http://${window.location.hostname}:3020`;

function App() {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedSnapshotId, setSelectedSnapshotId] = useState(null);
  const [filters, setFilters] = useState({
    search: '',
    packref: '',
    equipment: [],
    types: [],
    startDate: '',
    endDate: ''
  });

  // Carregar dados do snapshot selecionado
  useEffect(() => {
    if (!selectedSnapshotId) {
      setLoading(false);
      return;
    }

    const fetchSnapshotData = async () => {
      try {
        setLoading(true);
        let response;
        try {
          response = await fetch(`${API_BASE_URL}/snaps/${selectedSnapshotId}?page=1&size=9999`);
          if (!response.ok) throw new Error('Network response was not ok');
        } catch (fetchError) {
          console.warn('Falha ao buscar do servidor, tentando local sample-data.json...', fetchError);
          response = await fetch('/sample-data.json');
        }

        const data = await response.json();

        const rawItems = data.solution?.items || [];

        const parsedData = rawItems.map(task => {
          const parseDateTime = (val) => {
            if (val && typeof val === 'object' && val.$numberLong) {
              return parseInt(val.$numberLong, 10);
            }
            if (typeof val === 'string' || typeof val === 'number') {
              const num = Number(val);
              return isNaN(num) ? null : num;
            }
            return null;
          };

          const startVal = parseDateTime(task.start);
          const endVal = parseDateTime(task.end);
          const leadtime = Number(task.leadtime) || 0;
          const setuptime = Number(task.setuptime) || 0;

          return {
            ...task,
            start: startVal,
            end: endVal,
            leadtime,
            setuptime,
            _id: task._id && task._id.$oid ? task._id.$oid : task._id
          };
        });

        const allEquipments = Array.from(new Set(parsedData.map(task => String(task.equipment)))).sort();

        setTasks(parsedData);
        setFilters(prev => ({
          ...prev,
          equipment: allEquipments
        }));
      } catch (error) {
        console.error('Erro ao carregar dados do snapshot:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchSnapshotData();
  }, [selectedSnapshotId]);

  const handleSnapshotChange = (snapshotId) => {
    setSelectedSnapshotId(snapshotId);
    setTasks([]);
    setFilters(prev => ({
      ...prev,
      equipment: []
    }));
  };

  // Extrair valores únicos para filtros
  const { uniquePackrefs, uniqueEquipment, uniqueTypes } = useMemo(() => {
    const packrefs = new Set();
    const equipment = new Set();
    const types = new Set();

    tasks.forEach(task => {
      if (task.packref) packrefs.add(task.packref);
      equipment.add(task.equipment);
      types.add(task.type);
    });

    return {
      uniquePackrefs: Array.from(packrefs).sort((a, b) => a - b),
      uniqueEquipment: Array.from(equipment).sort(),
      uniqueTypes: Array.from(types).sort()
    };
  }, [tasks]);

  // Aplicar filtros
  const filteredTasks = useMemo(() => {
    return tasks.filter(task => {
      // Filtro de busca textual
      if (filters.search) {
        const searchLower = filters.search.toLowerCase();
        const matchSearch =
          String(task.order).includes(searchLower) ||
          String(task.product).includes(searchLower) ||
          String(task.operation).includes(searchLower) ||
          String(task.workflow).includes(searchLower);

        if (!matchSearch) return false;
      }

      // Filtro por packref
      if (filters.packref) {
        if (String(task.packref) !== filters.packref) return false;
      }

      // Filtro por equipamento
      if (filters.equipment.length > 0) {
        if (!filters.equipment.includes(String(task.equipment))) return false;
      }

      // Filtro por tipo
      if (filters.types.length > 0) {
        if (!filters.types.includes(task.type)) return false;
      }

      // Ignorar tarefas sem datas válidas (evita erro 'classList' no FrappeGantt)
      if (!task.start || !task.end || isNaN(new Date(task.start).getTime()) || isNaN(new Date(task.end).getTime())) {
        return false;
      }

      // Filtro de data
      if (filters.startDate) {
        const filterStartTs = new Date(filters.startDate).getTime();
        const taskEndTs = typeof task.end === 'number' ? task.end : new Date(task.end).getTime();
        if (taskEndTs < filterStartTs) return false;
      }

      if (filters.endDate) {
        // adiciona 1 dia em MS pra pegar o final do dia
        const filterEndTs = new Date(filters.endDate).getTime() + 86400000 - 1;
        const taskStartTs = typeof task.start === 'number' ? task.start : new Date(task.start).getTime();
        if (taskStartTs > filterEndTs) return false;
      }

      return true;
    });
  }, [tasks, filters]);

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-100 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4"></div>
          <p className="text-gray-600">{selectedSnapshotId ? 'Carregando dados do snapshot...' : 'Aguardando seleção do snapshot...'}</p>
        </div>
      </div>
    );
  }

  if (!selectedSnapshotId) {
    return (
      <div className="min-h-screen bg-gray-100 flex items-center justify-center">
        <div className="text-center max-w-md w-full px-4">
          <BarChart3 className="w-16 h-16 text-blue-600 mx-auto mb-4" />
          <h2 className="text-2xl font-bold text-gray-900 mb-2">Dashboard de Produção</h2>
          <p className="text-gray-600 mb-8">Selecione um snapshot para visualizar os dados de sequenciamento</p>

          <div className="flex justify-center">
            <SnapshotSelector
              selectedSnapshotId={selectedSnapshotId}
              onSnapshotChange={handleSnapshotChange}
            />
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-100">
      {/* Header */}
      <header className="bg-white shadow-sm border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <BarChart3 className="w-8 h-8 text-blue-600" />
              <div>
                <h1 className="text-2xl font-bold text-gray-900">
                  Dashboard de Produção
                </h1>
                <p className="text-sm text-gray-600">
                  Visualização de Sequenciamento de Workflows
                </p>
              </div>
            </div>
            <SnapshotSelector
              selectedSnapshotId={selectedSnapshotId}
              onSnapshotChange={handleSnapshotChange}
            />
          </div>
        </div>
      </header>

      {/* Conteúdo Principal */}
      <main className="max-w-7xl mx-auto px-4 py-6">
        {/* Estatísticas Rápidas */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
          <div className="bg-white rounded-lg shadow-md p-4">
            <div className="text-sm text-gray-600 mb-1">Total de Tarefas</div>
            <div className="text-2xl font-bold text-gray-900">{tasks.length}</div>
          </div>
          <div className="bg-white rounded-lg shadow-md p-4">
            <div className="text-sm text-gray-600 mb-1">Tarefas Filtradas</div>
            <div className="text-2xl font-bold text-blue-600">{filteredTasks.length}</div>
          </div>
          <div className="bg-white rounded-lg shadow-md p-4">
            <div className="text-sm text-gray-600 mb-1">Workflows Únicos</div>
            <div className="text-2xl font-bold text-gray-900">{uniqueEquipment.length}</div>
          </div>
          <div className="bg-white rounded-lg shadow-md p-4">
            <div className="text-sm text-gray-600 mb-1">Equipamentos</div>
            <div className="text-2xl font-bold text-gray-900">{uniqueEquipment.length}</div>
          </div>
        </div>

        {/* Painel de Filtros */}
        <FilterPanel
          filters={filters}
          setFilters={setFilters}
          uniquePackrefs={uniquePackrefs}
          uniqueEquipment={uniqueEquipment}
          uniqueTypes={uniqueTypes}
        />

        {/* Gráfico de Gantt Interativo */}
        <InteractiveGanttChart
          tasks={filteredTasks}
          onSave={(savedTasks) => {
            console.log('Tasks saved:', savedTasks);
            // Aqui você pode implementar a lógica de salvar
          }}
          onSimulationCreate={(simulation) => {
            console.log('Simulation created:', simulation);
            // Aqui você pode implementar a lógica de simulação
          }}
        />
      </main>

      {/* Footer */}
      <footer className="bg-white border-t border-gray-200 mt-8">
        <div className="max-w-7xl mx-auto px-4 py-4 text-center text-sm text-gray-600">
          Dashboard de Produção - Visualização Interativa de Workflows
        </div>
      </footer>
    </div>
  );
}

export default App;
