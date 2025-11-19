
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    llm_provider: str = Field(default="openai")
    openai_api_key: str | None = None
    openai_model: str = "gpt-4o-mini"
    openai_embed_model: str = "text-embedding-3-small"
    anthropic_api_key: str | None = None
    anthropic_model: str = "claude-3-5-sonnet-20240620"
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_key: str = "changeme"
    postgres_user: str = "app"
    postgres_password: str = "app"
    postgres_db: str = "pipelines"
    postgres_host: str = "postgres"
    postgres_port: int = 5432
    redis_host: str = "redis"
    redis_port: int = 6379
    weaviate_host: str = "weaviate"
    weaviate_port: int = 8080
    weaviate_scheme: str = "http"
    mlflow_tracking_uri: str = "http://mlflow:5000"
    log_level: str = "INFO"

settings = Settings()
