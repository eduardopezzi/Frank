# Dashboard de Produção - Packrefs

Aplicação React para visualização de sequenciamento de packrefs de produção usando gráfico de Gantt.

## 🚀 Funcionalidades

- **Gráfico de Gantt Interativo**: Visualização de packrefs ao longo do tempo
- **Filtragem Avançada**: 
  - Busca textual por ordem, produto, operação ou workflow
  - Filtro por packref específico
  - Seleção múltipla de equipamentos
  - Filtro por tipo (production/packaging)
- **Tooltips Detalhados**: Informações completas ao passar o mouse sobre cada packref
- **Cores Distintas**: Cada packref tem uma cor única e consistente
- **Responsivo**: Adaptável para diferentes tamanhos de tela
- **Estatísticas em Tempo Real**: Contagem de tarefas, packrefs e equipamentos

## 📦 Instalação

```bash
# Instalar dependências
npm install

# Iniciar servidor de desenvolvimento
npm run dev
```

A aplicação estará disponível em `http://localhost:5173/`

## 🏗️ Estrutura do Projeto

```
gantt-dashboard/
├── data/
│   └── sample-data.json      # Dados de exemplo
├── src/
│   ├── components/
│   │   ├── GanttChart.jsx    # Componente principal do gráfico
│   │   ├── FilterPanel.jsx   # Painel de filtros
│   │   └── TaskBar.jsx       # Barra individual de tarefa
│   ├── App.jsx               # Componente principal
│   └── index.css             # Estilos globais
└── public/
    └── sample-data.json      # Dados acessíveis via HTTP
```

## 📊 Estrutura dos Dados

Cada tarefa possui a seguinte estrutura:

```json
{
  "order": 47500,
  "type": "production",
  "packref": 1526878,
  "deadline": 1771372800000.0,
  "workflow": 168742,
  "equipment": "812",
  "sector": 0,
  "operation": 22,
  "product": 36610,
  "leadtime": 10200000.0,
  "setuptime": 600000.0,
  "start": 1771495200000,
  "end": 1771505400000
}
```

### Campos Principais

- **order**: Número da ordem de produção
- **type**: Tipo da operação (production/packaging)
- **packref**: Identificador do pacote (pode ser null para packaging)
- **equipment**: Equipamento onde a operação ocorre
- **start**: Timestamp de início (milissegundos)
- **end**: Timestamp de fim (milissegundos)
- **product**: ID do produto
- **operation**: Número da operação
- **workflow**: ID do workflow
- **leadtime**: Tempo de duração em milissegundos
- **setuptime**: Tempo de setup em milissegundos

## 🎨 Como Usar

1. **Visualização Geral**: 
   - Eixo X: linha do tempo com datas
   - Eixo Y: equipamentos agrupados
   - Barras coloridas representam cada packref

2. **Filtragem**:
   - Use o campo de busca para encontrar ordens, produtos ou operações
   - Selecione packrefs específicos no dropdown
   - Clique nos equipamentos para filtrar visualização
   - Use os botões de tipo (Production/Packaging)

3. **Interação**:
   - Passe o mouse sobre as barras para ver detalhes completos
   - Use "Limpar Filtros" para resetar todas as seleções

4. **Escala de Tempo**:
   - O gráfico ajusta automaticamente a escala baseada no range de dados
   - Linhas verticais indicam marcos temporais

## 🛠️ Tecnologias Utilizadas

- **React**: Framework JavaScript
- **Vite**: Bundler e servidor de desenvolvimento
- **Tailwind CSS**: Framework de estilização
- **date-fns**: Manipulação de datas
- **lucide-react**: Ícones da interface

## 📝 Personalização

### Adicionar Novos Dados

Substitua o arquivo `data/sample-data.json` com seus dados ou crie uma API para fornecer os dados.

### Modificar Cores

Edite a função `getColorFromPackref` em `src/components/TaskBar.jsx` para alterar a lógica de geração de cores.

### Ajustar Escala de Tempo

Modifique a lógica em `src/components/GanttChart.jsx` na função `timeMarkers` para ajustar os intervalos de tempo.

## 🚀 Build para Produção

```bash
# Criar build otimizado
npm run build

# Preview do build
npm run preview
```

## 📄 Licença

Este projeto foi desenvolvido para visualização de sequenciamento de produção.