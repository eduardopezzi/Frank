# 🎨 Frank Rendering Engine API

Motor de renderização baseado no Blender Cycles com API REST, fila assíncrona, suporte a glTF/GLB e catálogo de materiais PBR.

## Arquitetura

```
[Client]
   ↓ POST /render (upload .glb ou .gltf)
[FastAPI API]
   ↓ Enqueue job
[Redis] ←→ [Celery Worker]
   ↓           ↓
   ↓    [Blender Cycles CLI]
   ↓    (Importação e renderização GLB/GLTF)
   ↓           ↓
[GET /status]  [outputs/*.png]
   ↓
[GET /download → PNG]
```

## Stack

| Componente | Tecnologia |
|---|---|
| API | FastAPI + Uvicorn |
| Fila | Celery + Redis |
| Renderização | Blender Cycles (headless) |
| Materiais | JSON Catalog (PBR) |
| Containers | Docker Compose |

## Requisitos

- Python 3.11+
- Redis (para fila de tarefas)
- Blender 4.0+ (para o worker)
- Docker & Docker Compose (para deploy)

## Instalação (desenvolvimento local)

### 1. Ambiente Python

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Variáveis de ambiente

```bash
cp .env.example .env
# Editar .env conforme necessário
```

### 3. Iniciar Redis

```bash
# Via Docker
docker run -d --name Frank-redis -p 6379:6379 redis:7-alpine

# Ou se já tiver Redis instalado
redis-server
```

### 4. Iniciar a API

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 5. Iniciar o Worker

```bash
celery -A worker.celery_app worker --loglevel=info
```

## Deploy com Docker Compose

```bash
docker-compose up -d
```

Acesse:
- **API**: http://localhost:8000
- **Swagger UI**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## Endpoints

### Renderização

| Método | Endpoint | Descrição |
|---|---|---|
| `POST` | `/render` | Upload de .glb e iniciar render |
| `GET` | `/render/status/{job_id}` | Status do job |
| `GET` | `/render/download/{job_id}` | Download da imagem |

### Materiais PBR

| Método | Endpoint | Descrição |
|---|---|---|
| `POST` | `/materials` | Criar material |
| `GET` | `/materials` | Listar catálogo |
| `GET` | `/materials/{id}` | Detalhe do material |
| `PUT` | `/materials/{id}` | Atualizar material |
| `DELETE` | `/materials/{id}` | Remover material |

## Uso

### Enviar render

```bash
curl -X POST http://localhost:8000/render \
  -F "file=@meu_modelo.glb" \
  -F "samples=128" \
  -F "resolution_x=1920" \
  -F "resolution_y=1080"
```

Resposta:
```json
{
  "job_id": "abc-123",
  "status": "pending",
  "message": "Render job enqueued"
}
```

### Verificar status

```bash
curl http://localhost:8000/render/status/abc-123
```

### Download da imagem

```bash
curl -O http://localhost:8000/render/download/abc-123
```

## Formatos Suportados

### glTF/GLB (Recomendado)
- **Arquivos aceitos:** `.glb`, `.gltf`
- **Vantagens:** Formato nativo do Blender, suporte completo a materiais PBR, texturas embutidas
- **Como converter:**
  - **SketchUp:** File → Export → glTF 2.0
  - **Rhino 3D:** File → Export Selected → glTF
  - **3DS Max:** File → Export → glTF
  - **Fusion 360:** File → Export → glTF

### SketchUp (.skp) — **Não suportado diretamente**
Arquivos `.skp` não são suportados diretamente devido a incompatibilidades com Blender 4.0.

**Solução:**
1. Abra o arquivo `.skp` no SketchUp
2. Vá em **File → Export → glTF 2.0**
3. Carregue o arquivo `.glb` ou `.gltf` gerado na API

**Converters online alternativos:**
- [Sketchfab](https://sketchfab.com/) — Upload SKP → Download GLB
- [Online 3D Converter](https://www.online3dconverter.com/) — SKP → GLB

## Catálogo de Materiais PBR

O catálogo vem com materiais comuns para projetos de arquitetura:

- **Concreto** (aparente, polido)
- **Madeira** (taco, MDF, compensado)
- **Vidro** (transparente, fumê)
- **Metal** (aço inox, alumínio)
- **Parede** (reboco, tijolo)
- **Piso** (cerâmica, porcelanato)

### Exemplo de material

```json
{
  "material_id": "wood_taco_01",
  "name": "Taco de Madeira",
  "category": "wood",
  "tags": ["floor", "interior", "warm"],
  "pbr_properties": {
    "base_color": [0.45, 0.28, 0.14, 1.0],
    "roughness": 0.35,
    "metallic": 0.0,
    "normal_map": null,
    "emission": 0.0
  }
}
```

## Roadmap

- [x] API REST com FastAPI
- [x] Fila assíncrona com Celery + Redis
- [x] Script Blender com auto-framing e iluminação
- [x] Catálogo de materiais PBR
- [x] Docker Compose
- [ ] Integração com IA para descrição de cenas
- [ ] Suporte a HDRI environments
- [ ] Preview rápido (Eevee) antes do render final
- [ ] Suporte a múltiplos ângulos de câmera
- [ ] Upload de texturas customizadas
- [ ] Webhook para notificação de render completo
- [ ] Storage Cloud services (TBD - AWS S3, Google Cloud 
Storage, etc.) para produção
- [ ] Authentication and Authorization: criate a user access with login and register and create a role admin. Think to use some google oauth to make it more easy to use. 
    
- [ ] UI/UX Improvement:
    - [ ] Responsive design
    - [ ] Drag and drop improvement
    - [ ] Notifications
    - [x] create a gallery of rendered images
    - [x] Add a feature to select a material from the catalog and apply it to the model
    - [ ] create a feature to save the rendered image to a file
    - [ ] create a feature to rate the rendered image
    - [ ] create a feature to create projects and save the rendered images to the project and materials (PRB also)
    - [x] 3D Preview interativo: visualização do modelo 3D com zoom, rotação e posicionamento de câmera para definir ângulo e enquadramento exatos antes do render
    - [x] organizar as sessoes da pagina em abas: como aba com galeria dos rennders passados, aba com os materiais que serao utilizado no render ou projeto, fila de processos, etc 

## Licença

Uso interno.
