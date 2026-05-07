"""
SQLAlchemy ORM Models for Projects, RenderJobs, and Materials.
"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON, Float
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid

from app.database import Base

from sqlalchemy import Table

# Association table for Many-to-Many relationship
project_materials = Table(
    "project_materials",
    Base.metadata,
    Column("project_id", String, ForeignKey("projects.id"), primary_key=True),
    Column("material_id", String, ForeignKey("materials.id"), primary_key=True),
    Column("assigned_at", DateTime, default=datetime.utcnow)
)

class Project(Base):
    __tablename__ = "projects"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    jobs = relationship("RenderJob", back_populates="project", cascade="all, delete-orphan")
    materials = relationship("Material", secondary=project_materials, back_populates="projects")

class RenderJob(Base):
    __tablename__ = "render_jobs"

    id = Column(String, primary_key=True, index=True)
    project_id = Column(String, ForeignKey("projects.id"), nullable=True)
    status = Column(String, default="pending")
    original_filename = Column(String, nullable=True)
    file_size = Column(Integer, nullable=True)
    input_path = Column(String, nullable=False)
    output_path = Column(String, nullable=True)
    render_settings = Column(JSON, nullable=True)
    rating = Column(Integer, default=0)
    error_message = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)

    project = relationship("Project", back_populates="jobs")

class Material(Base):
    __tablename__ = "materials"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    category = Column(String, index=True)
    pbr_data = Column(JSON, nullable=False)
    thumbnail_path = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    projects = relationship("Project", secondary=project_materials, back_populates="materials")
