
import weaviate
from src.utils.config import settings

CLASS_NAME = "RunbookChunk"

def client():
    url = f"{settings.weaviate_scheme}://{settings.weaviate_host}:{settings.weaviate_port}"
    return weaviate.Client(url)

def ensure_schema():
    c = client()
    if not c.schema.exists(CLASS_NAME):
        c.schema.create_class({
            "class": CLASS_NAME,
            "vectorizer": "none",
            "properties": [
                {"name":"text","dataType":["text"]},
                {"name":"pipeline","dataType":["string"]},
                {"name":"topic","dataType":["string"]},
            ]
        })

def upsert(payloads, vectors):
    c = client()
    with c.batch() as b:
        for p,v in zip(payloads, vectors):
            b.add_data_object(p, CLASS_NAME, vector=v)

def search(vec, limit=5):
    c = client()
    return c.query.get(CLASS_NAME, ["text","pipeline","topic"]).with_near_vector({"vector":vec}).with_limit(limit).do()
