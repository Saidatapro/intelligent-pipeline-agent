
from src.rag.retriever import retrieve
def analyze(pipeline_id: int, symptoms: dict) -> dict:
    q = f"Root cause for pipeline {pipeline_id} with {symptoms}"
    ctx = retrieve(q, k=5)
    return {"contexts": ctx, "hypothesis": "Possible resource saturation or schema drift."}
