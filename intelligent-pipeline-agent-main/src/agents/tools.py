
from src.database.session import SessionLocal
from src.database import models

def record_incident(pipeline_id: int, severity: str, summary: str, details: dict) -> int:
    with SessionLocal() as s:
        obj = models.Incident(pipeline_id=pipeline_id, severity=severity, summary=summary, details=details)
        s.add(obj); s.commit(); s.refresh(obj); return obj.id

def create_recommendation(pipeline_id: int, action: str, rationale: str) -> int:
    with SessionLocal() as s:
        # store in incidents for brevity or add a separate table; minimal demo keeps incidents/recs simple
        rec = models.Incident(pipeline_id=pipeline_id, severity="note", summary=action, details={"rationale":rationale}, status="recommendation")
        s.add(rec); s.commit(); s.refresh(rec); return rec.id
