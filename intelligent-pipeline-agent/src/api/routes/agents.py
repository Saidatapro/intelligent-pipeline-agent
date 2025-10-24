
from fastapi import APIRouter, Depends
from src.api.dependencies import require_api_key
from src.agents.orchestrator import run_once

router = APIRouter(prefix="/api/v1/agents", tags=["agents"])

@router.post("/trigger", dependencies=[Depends(require_api_key)])
def trigger(pipeline_id: int, approved: bool = False):
    return run_once(pipeline_id=pipeline_id, approved=approved)
