
from prometheus_client import Counter, Gauge, generate_latest, CONTENT_TYPE_LATEST
from fastapi import Response
pipeline_errors_total = Counter("pipeline_errors_total","Total errors",["pipeline"])
pipeline_latency_ms = Gauge("pipeline_latency_ms","Last run latency",["pipeline"])
agent_actions_total = Counter("agent_actions_total","Agent actions",["agent","action"])
def metrics_response():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
