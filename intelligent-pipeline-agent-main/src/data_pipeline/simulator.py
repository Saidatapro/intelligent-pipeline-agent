
import random, time
from src.database.session import SessionLocal, engine, Base
from src.database import models
from src.monitoring.prometheus_exporter import pipeline_errors_total, pipeline_latency_ms

PIPELINES=[
    {"name":"s3_to_dwh","source":"s3","destination":"warehouse"},
    {"name":"pg_cdc_to_lake","source":"postgres","destination":"lake"},
    {"name":"api_ingest","source":"api","destination":"lake"},
    {"name":"kafka_batch","source":"kafka","destination":"warehouse"},
    {"name":"file_drop","source":"fs","destination":"lake"},
]

def ensure_db():
    Base.metadata.create_all(bind=engine)
    with SessionLocal() as s:
        for p in PIPELINES:
            if not s.query(models.Pipeline).filter_by(name=p["name"]).first():
                s.add(models.Pipeline(name=p["name"], source=p["source"], destination=p["destination"]))
        s.commit()

def tick():
    with SessionLocal() as s:
        for p in s.query(models.Pipeline).all():
            dur = random.uniform(100, 2000) * (2 if random.random()<0.1 else 1)
            err = 0 if random.random()>0.85 else random.randint(1,5)
            rec = random.randint(1000, 100000)
            mem = random.uniform(100, 2000)
            m = models.Metric(pipeline_id=p.id, records=rec, duration_ms=dur, errors=err, memory_mb=mem)
            s.add(m); s.commit()
            pipeline_latency_ms.labels(pipeline=p.name).set(dur)
            if err: pipeline_errors_total.labels(pipeline=p.name).inc(err)

def main_loop():
    ensure_db()
    while True:
        tick()
        time.sleep(5)

if __name__ == "__main__":
    main_loop()
