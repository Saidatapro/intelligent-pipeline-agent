
from fastapi import FastAPI
from src.api.middleware import add_cors
from src.api.routes import pipelines, agents, metrics, websocket
from src.database.session import Base, engine

app = FastAPI(title="Intelligent Pipeline Agent", version="1.0.0")
add_cors(app)
Base.metadata.create_all(bind=engine)
app.include_router(pipelines.router)
app.include_router(agents.router)
app.include_router(metrics.router)
app.include_router(websocket.router)

@app.get("/healthz")
def healthz(): return {"ok": True}
