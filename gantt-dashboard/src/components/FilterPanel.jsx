import { Search, X, Filter } from 'lucide-react';

const FilterPanel = ({
  filters,
  setFilters,
  uniquePackrefs,
  uniqueEquipment,
  uniqueTypes
}) => {
  const handleFilterChange = (key, value) => {
    setFilters(prev => ({
      ...prev,
      [key]: value
    }));
  };

  const toggleEquipment = (equipment) => {
    setFilters(prev => ({
      ...prev,
      equipment: prev.equipment.includes(equipment)
        ? prev.equipment.filter(e => e !== equipment)
        : [...prev.equipment, equipment]
    }));
  };

  const toggleType = (type) => {
    setFilters(prev => ({
      ...prev,
      types: prev.types.includes(type)
        ? prev.types.filter(t => t !== type)
        : [...prev.types, type]
    }));
  };

  const clearFilters = () => {
    setFilters({
      search: '',
      packref: '',
      equipment: [],
      types: [],
      startDate: '',
      endDate: ''
    });
  };

  const hasActiveFilters = filters.search || filters.packref ||
    filters.equipment.length > 0 || filters.types.length > 0 ||
    filters.startDate || filters.endDate;

  return (
    <div className="bg-white rounded-lg shadow-md p-4 mb-4">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-2">
          <Filter className="w-5 h-5 text-blue-600" />
          <h2 className="text-lg font-semibold text-gray-800">Filtros</h2>
        </div>
        {hasActiveFilters && (
          <button
            onClick={clearFilters}
            className="flex items-center gap-1 text-sm text-red-600 hover:text-red-700 transition-colors"
          >
            <X className="w-4 h-4" />
            Limpar Filtros
          </button>
        )}
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {/* Busca textual */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Busca
          </label>
          <div className="relative">
            <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-gray-400" />
            <input
              type="text"
              placeholder="Ordem, produto..."
              value={filters.search}
              onChange={(e) => handleFilterChange('search', e.target.value)}
              className="w-full pl-10 pr-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent text-sm"
            />
          </div>
        </div>

        {/* Filtro por Packref */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Packref
          </label>
          <select
            value={filters.packref}
            onChange={(e) => handleFilterChange('packref', e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent text-sm"
          >
            <option value="">Todos</option>
            {uniquePackrefs.map(packref => (
              <option key={packref} value={packref}>
                {packref}
              </option>
            ))}
          </select>
        </div>

        {/* Filtro por Tipo */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            Tipo
          </label>
          <div className="flex gap-2">
            {uniqueTypes.map(type => (
              <button
                key={type}
                onClick={() => toggleType(type)}
                className={`px-3 py-1.5 rounded-lg text-sm font-medium transition-colors ${filters.types.includes(type)
                    ? 'bg-blue-600 text-white'
                    : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                  }`}
              >
                {type.charAt(0).toUpperCase() + type.slice(1)}
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* Datas */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4">
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Data Início
          </label>
          <input
            type="date"
            value={filters.startDate || ''}
            onChange={(e) => handleFilterChange('startDate', e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 text-sm"
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Data Fim
          </label>
          <input
            type="date"
            value={filters.endDate || ''}
            onChange={(e) => handleFilterChange('endDate', e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 text-sm"
          />
        </div>
      </div>

      {/* Filtro por Equipamento */}
      <div className="mt-4">
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Equipamentos
        </label>
        <div className="max-h-32 overflow-y-auto border border-gray-200 rounded-lg p-2 bg-gray-50">
          <div className="flex flex-wrap gap-2">
            {uniqueEquipment.map(equipment => (
              <button
                key={equipment}
                onClick={() => toggleEquipment(equipment)}
                className={`px-3 py-1 rounded-md text-sm font-medium transition-colors ${filters.equipment.includes(equipment)
                    ? 'bg-green-600 text-white'
                    : 'bg-white text-gray-700 hover:bg-gray-100 border border-gray-300'
                  }`}
              >
                {equipment}
              </button>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default FilterPanel;