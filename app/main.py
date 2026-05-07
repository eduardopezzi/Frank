"""
FastAPI application entry point.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.config import settings
from app.routers import render, materials, ai_design


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown events."""
    # Startup: ensure directories exist
    settings.ensure_directories()
    yield
    # Shutdown: cleanup if needed


app = FastAPI(
    title="Frank Rendering Engine",
    description=(
        "API REST para renderização de modelos 3D (.glb) "
        "via Blender Cycles com fila assíncrona e catálogo de materiais PBR."
    ),
    version="0.1.0",
    lifespan=lifespan,
)

# CORS — allow all origins in dev (restrict in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure directories exist before mounting
settings.ensure_directories()

# Routers
app.include_router(render.router, prefix="/render", tags=["Rendering"])
app.include_router(materials.router, prefix="/materials", tags=["Materials"])
app.include_router(ai_design.router, prefix="/ai", tags=["AI Design"])

# Static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.mount("/textures", StaticFiles(directory=settings.textures_dir), name="textures")


@app.get("/health", tags=["System"])
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": "Frank-rendering-engine",
        "version": "0.1.0",
    }


@app.get("/", tags=["UI"])
async def root():
    """Serve the dashboard UI."""
    return FileResponse("app/static/index.html")
