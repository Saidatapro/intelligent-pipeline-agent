
def optimize(pipeline_id: int, analysis: dict) -> dict:
    actions = ["Enable exponential backoff (max 5 retries)", "Increase parallelism by +1 worker"]
    if "schema" in (analysis.get("hypothesis","").lower()):
        actions.append("Run schema migration & backfill 1h")
    return {"actions": actions, "auto_safe": ["Enable exponential backoff (max 5 retries)"]}
