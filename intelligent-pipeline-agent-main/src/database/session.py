
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from src.utils.config import settings

class Base(DeclarativeBase): pass

def _url():
    s = settings
    # return f"postgresql://{s.postgres_user}:{s.postgres_password}@{s.postgres_host}:{s.postgres_port}/{s.postgres_db}"
    return "sqlite:///./pipelines.db"

engine = create_engine(_url(), connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
