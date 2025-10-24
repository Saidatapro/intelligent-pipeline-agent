
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Float, Boolean, JSON, DateTime, ForeignKey
from sqlalchemy.sql import func
from .session import Base

class Pipeline(Base):
    __tablename__ = "pipelines"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True)
    source: Mapped[str] = mapped_column(String)
    destination: Mapped[str] = mapped_column(String)
    enabled: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())

class Metric(Base):
    __tablename__ = "metrics"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    pipeline_id: Mapped[int] = mapped_column(Integer, ForeignKey("pipelines.id"))
    timestamp = mapped_column(DateTime(timezone=True), server_default=func.now())
    records: Mapped[int] = mapped_column(Integer, default=0)
    duration_ms: Mapped[float] = mapped_column(Float, default=0.0)
    errors: Mapped[int] = mapped_column(Integer, default=0)
    memory_mb: Mapped[float] = mapped_column(Float, default=0.0)

class Incident(Base):
    __tablename__ = "incidents"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    pipeline_id: Mapped[int] = mapped_column(Integer)
    severity: Mapped[str] = mapped_column(String)
    summary: Mapped[str] = mapped_column(String)
    details: Mapped[dict] = mapped_column(JSON, default={})
    status: Mapped[str] = mapped_column(String, default="open")
