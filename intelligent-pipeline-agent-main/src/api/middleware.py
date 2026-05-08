import os
from starlette.middleware.cors import CORSMiddleware


def _get_allowed_origins() -> list[str]:
    raw = os.getenv("CORS_ALLOWED_ORIGINS", "")
    origins = [origin.strip() for origin in raw.split(",") if origin.strip()]
    # Local development defaults; production should set CORS_ALLOWED_ORIGINS.
    return origins or ["http://localhost:3000", "http://localhost:8501"]


def add_cors(app) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=_get_allowed_origins(),
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
        allow_headers=["*"],
    )
