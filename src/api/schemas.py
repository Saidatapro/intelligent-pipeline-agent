
from pydantic import BaseModel, Field
from typing import Dict

class PipelineIn(BaseModel):
    name: str
    source: str
    destination: str

class PipelineOut(PipelineIn):
    id: int
    enabled: bool

class HealthOut(BaseModel):
    status: str
    health_score: float
    metrics: Dict[str, float]
