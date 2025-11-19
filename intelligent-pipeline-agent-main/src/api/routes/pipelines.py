
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.api.schemas import PipelineIn, PipelineOut, HealthOut
from src.api.dependencies import require_api_key
from src.database.session import SessionLocal
from src.database import models
from src.agents.monitor_agent import compute_health

router = APIRouter(prefix="/api/v1/pipelines", tags=["pipelines"])

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.post("", response_model=PipelineOut, dependencies=[Depends(require_api_key)])
def register_pipeline(p: PipelineIn, db: Session = Depends(get_db)):
    obj = models.Pipeline(name=p.name, source=p.source, destination=p.destination)
    db.add(obj); db.commit(); db.refresh(obj)
    return PipelineOut(id=obj.id, name=obj.name, source=obj.source, destination=obj.destination, enabled=obj.enabled)

@router.get("/{pid}/health", response_model=HealthOut)
def get_health(pid: int):
    h = compute_health(pid)
    return HealthOut(status=h["status"], health_score=h["health_score"], metrics=h["metrics"])
