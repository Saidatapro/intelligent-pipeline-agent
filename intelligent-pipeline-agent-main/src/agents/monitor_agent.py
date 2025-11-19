
from sqlalchemy import text
from src.database.session import SessionLocal

def compute_health(pipeline_id: int) -> dict:
    # avg over last 10
    with SessionLocal() as s:
        rows = s.execute(text("""
            SELECT avg(duration_ms), avg(errors), avg(memory_mb), avg(records)
            FROM (SELECT duration_ms, errors, memory_mb, records
                  FROM metrics WHERE pipeline_id=:pid ORDER BY id DESC LIMIT 10) t
        """), {"pid": pipeline_id}).fetchone()
        if not rows or rows[3] is None: return {"status":"unknown","health_score":0.0,"metrics":{}}
        dur, err, mem, rec = rows
        score = max(0.0, 100.0 - (dur or 0)/50.0 - (err or 0)*10.0 - (mem or 0)/200.0)
        st = "ok" if score>80 else "degraded" if score>60 else "bad"
        return {"status":st,"health_score":round(score,2),"metrics":{"duration_ms":dur or 0,"errors":err or 0,"records":rec or 0}}
