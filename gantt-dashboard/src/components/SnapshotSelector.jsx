import { useState, useEffect, useCallback } from 'react';
import { ChevronDown, Database, Search, X, Loader2 } from 'lucide-react';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || `http://${window.location.hostname}:3020`;

export default function SnapshotSelector({ selectedSnapshotId, onSnapshotChange }) {
  const [snapshots, setSnapshots] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searching, setSearching] = useState(false);
  const [isOpen, setIsOpen] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');

  const fetchSnapshots = useCallback(async (search = '') => {
    try {
      if (search) setSearching(true);
      else setLoading(true);

      const response = await fetch(`${API_BASE_URL}/snaps/?page=1&size=100&search=${encodeURIComponent(search)}`);
      const data = await response.json();
      setSnapshots(data.items || []);
    } catch (error) {
      console.warn('Erro ao carregar snapshots do servidor, usando local dummy:', error);
      setSnapshots([{
        _id: 'local-sample',
        metadata: { name: 'Local Sample Data' },
        count: 6332,
        status: 'FEASIBLE',
        created: Date.now()
      }]);
    } finally {
      setLoading(false);
      setSearching(false);
    }
  }, []);

  useEffect(() => {
    fetchSnapshots();
  }, [fetchSnapshots]);

  // Debounce para busca
  useEffect(() => {
    if (searchTerm === '') {
      fetchSnapshots('');
      return;
    }

    const delayDebounceFn = setTimeout(() => {
      fetchSnapshots(searchTerm);
    }, 500);

    return () => clearTimeout(delayDebounceFn);
  }, [searchTerm, fetchSnapshots]);

  const selectedSnapshot = snapshots.find(s => s._id === selectedSnapshotId);

  if (loading && !isOpen) {
    return (
      <div className="flex items-center gap-2 text-gray-500">
        <Database className="w-4 h-4" />
        <span>Carregando snapshots...</span>
      </div>
    );
  }

  return (
    <div className="relative">
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="flex items-center gap-2 px-4 py-2 bg-white border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors min-w-[300px]"
      >
        <Database className="w-4 h-4 text-blue-600" />
        <div className="flex-1 text-left truncate">
          <span className="text-sm text-gray-600 block">Snapshot:</span>
          <span className="font-medium text-gray-900 truncate block">
            {selectedSnapshot?.metadata?.name || 'Selecione um snapshot'}
          </span>
        </div>
        <ChevronDown className={`w-4 h-4 text-gray-500 transition-transform ${isOpen ? 'rotate-180' : ''}`} />
      </button>

      {isOpen && (
        <div className="absolute top-full right-0 mt-2 bg-white border border-gray-200 rounded-lg shadow-lg z-50 overflow-hidden flex flex-col max-h-[500px] w-[400px] right-0 md:left-0 md:right-auto">
          {/* Campo de Busca dentro do Dropdown */}
          <div className="p-2 border-b border-gray-100 bg-gray-50">
            <div className="relative">
              <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-gray-400" />
              <input
                type="text"
                autoFocus
                placeholder="Buscar snapshot..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="w-full pl-9 pr-8 py-2 bg-white border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              />
              {searchTerm && (
                <button
                  onClick={() => setSearchTerm('')}
                  className="absolute right-2 top-1/2 transform -translate-y-1/2 p-1 hover:bg-gray-100 rounded-full"
                >
                  <X className="w-3 h-3 text-gray-400" />
                </button>
              )}
            </div>
          </div>

          <div className="overflow-y-auto flex-1">
            {searching ? (
              <div className="px-4 py-8 text-center text-gray-500 flex flex-col items-center gap-2">
                <Loader2 className="w-6 h-6 animate-spin text-blue-600" />
                <span>Buscando snapshots...</span>
              </div>
            ) : snapshots.length === 0 ? (
              <div className="px-4 py-8 text-center text-gray-500">
                {searchTerm ? `Nenhum snapshot encontrado para "${searchTerm}"` : 'Nenhum snapshot disponível'}
              </div>
            ) : (
              snapshots.map(snapshot => (
                <button
                  key={snapshot._id}
                  onClick={() => {
                    onSnapshotChange(snapshot._id);
                    setIsOpen(false);
                  }}
                  className={`w-full px-4 py-3 text-left hover:bg-gray-50 transition-colors border-b border-gray-100 last:border-b-0 ${selectedSnapshotId === snapshot._id ? 'bg-blue-50 border-l-4 border-l-blue-600' : ''
                    }`}
                >
                  <div className="font-medium text-gray-900">{snapshot.metadata?.name || 'Sem nome'}</div>
                  <div className="text-sm text-gray-500 mt-1 flex items-center gap-2">
                    <span>ID: {snapshot._id.substring(0, 8)}...</span>
                    <span>•</span>
                    <span>{snapshot.count} tarefas</span>
                    <span>•</span>
                    <span className={snapshot.status === 'FEASIBLE' ? 'text-green-600' : 'text-red-600'}>
                      {snapshot.status}
                    </span>
                  </div>
                  <div className="text-xs text-gray-400 mt-1">
                    Criado em: {new Date(snapshot.created).toLocaleString('pt-BR')}
                  </div>
                </button>
              ))
            )}
          </div>
        </div>
      )}
    </div>
  );
}
