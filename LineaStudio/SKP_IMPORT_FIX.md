# Correção do Problema de Importação SKP

## Problema Original
```
RuntimeError: SKP Import failed: Error: Add-on not loaded: "sketchup_importer", 
cause: No module named 'sketchup_importer'
```

## Causas Raiz Identificadas

1. **`--factory-startup` no comando Blender** (`worker/tasks.py` linha 79):
   - Esta flag faz o Blender iniciar com configurações de fábrica
   - Impede o escaneamento e registro automático de addons instalados
   - Quando o script tenta `bpy.ops.preferences.addon_enable()`, o Blender não encontra o módulo

2. **Carregamento insuficiente do addon** (`worker/blender_scripts/render_gltf.py`):
   - O script não adicionava o path dos addons ao `sys.path` do Python
   - Não usava `addon_utils.modules(refresh=True)` para forçar o rediscovery
   - Não tinha um fallback caso o método padrão falhasse

## Soluções Implementadas

### 1. Dockerfile.worker
- **Adicionado verificação pós-instalação**: `ls -la` para confirmar que os arquivos do addon foram extraídos corretamente
- Isso ajuda a identificar problemas de estrutura do repositório durante o build

### 2. worker/blender_scripts/render_gltf.py
Implementado um carregamento robusto do addon em múltiplas camadas:

#### Camada 1: Método Padrão com Refresh
```python
import addon_utils
addon_path = "/usr/local/blender/4.0/scripts/addons"

# Adicionar ao sys.path
if addon_path not in sys.path:
    sys.path.insert(0, addon_path)

# Forçar rediscovery dos addons
addon_utils.modules(refresh=True)

# Habilitar o addon
if not addon_utils.check("sketchup_importer")[0]:
    bpy.ops.preferences.addon_enable(module="sketchup_importer")
```

#### Camada 2: Fallback - Import Direto e Registro Manual
Se o método padrão falhar, o script tenta:
```python
import importlib
sketchup_importer = importlib.import_module("sketchup_importer")

# Registrar manualmente se necessário
if hasattr(sketchup_importer, 'register'):
    sketchup_importer.register()
```

#### Camada 3: Logging Detalhado
- Mensagens de debug em cada etapa
- Traceback completo em caso de erro

### 3. worker/tasks.py
- **Removida a flag `--factory-startup`** do comando Blender
- O script já faz `bpy.ops.wm.read_factory_settings(use_empty=True)` para limpar a cena
- Sem `--factory-startup`, o Blender carrega os addons instalados normalmente

## Fluxo Atual

```
Arquivo SKP
    ↓
Worker recebe task
    ↓
Blender inicia SEM --factory-startup
    ↓
render_gltf.py detecta extensão .skp
    ↓
[Camada 1] Adiciona path ao sys.path
    ↓
[Camada 1] Refresh dos módulos de addon
    ↓
[Camada 1] Habilita sketchup_importer via addon_enable
    ↓
[Se falhar] → [Camada 2] Import direto via importlib
    ↓
[Se falhar] → [Camada 2] Registro manual com register()
    ↓
Import SKP via bpy.ops.import_scene.skp()
    ↓
Render Cycles
    ↓
PNG de saída
```

## Comandos Úteis

### Rebuild do worker
```bash
docker-compose build worker
docker-compose up -d worker
```

### Verificar logs
```bash
docker-compose logs worker -f
```

### Verificar instalação do addon no container
```bash
docker exec -it cycles-worker ls -la /usr/local/blender/4.0/scripts/addons/sketchup_importer/
```

### Testar importação manual no container
```bash
docker exec -it cycles-worker /usr/local/blender/blender -b -P /app/worker/blender_scripts/render_gltf.py -- /app/arquivo_teste.skp /app/output.png '{}'
```

## Notas Importantes

1. **O addon `sketchup_importer` do Starrigger requer bibliotecas nativas do SketchUp SDK**
   - Se o erro persistir, pode ser necessário instalar dependências adicionais no Dockerfile
   - Verificar se as bibliotecas `.so` estão presentes no addon

2. **Alternativa: Conversão prévia via Assimp**
   - Se o addon continuar falhando, considerar implementar um pipeline alternativo:
     - SKP → (assimp) → GLB → (Blender) → PNG
   - Requer instalação do `assimp-utils` e compilação com suporte a SKP

3. **Performance**
   - A limpeza de cena agora é feita pelo script, não pelo `--factory-startup`
   - Isso tem o mesmo efeito, mas permite carregamento de addons

## Testando a Solução

1. Faça upload de um arquivo `.skp` pela API
2. Verifique os logs do worker para confirmar:
   ```
   [Cycles] Added /usr/local/blender/4.0/scripts/addons to sys.path
   [Cycles] Refreshed addon modules
   [Cycles] Enabling sketchup_importer addon...
   [Cycles] sketchup_importer addon enabled
   [Cycles] SKP file imported successfully
   ```
3. O arquivo PNG deve ser gerado na pasta `outputs/`