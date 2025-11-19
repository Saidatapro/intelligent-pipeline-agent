
from fastapi import APIRouter
from src.monitoring.prometheus_exporter import metrics_response
router = APIRouter(prefix="/api/v1", tags=["metrics"])
@router.get("/metrics")
def metrics(): return metrics_response()
