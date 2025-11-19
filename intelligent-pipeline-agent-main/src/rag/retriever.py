
from .document_loader import chunk_text
from .embeddings import embed_texts
from .vector_store import ensure_schema, upsert, search

def index_runbooks(runbooks: list[dict]):
    ensure_schema()
    chunks, payloads = [], []
    for d in runbooks:
        for c in chunk_text(d["text"]):
            chunks.append(c); payloads.append({"text":c,"pipeline":"*","topic":"runbook"})
    vecs = embed_texts(chunks)
    upsert(payloads, vecs)

def retrieve(query: str, k:int=5) -> list[str]:
    qv = embed_texts([query])[0]
    res = search(qv, limit=k)
    data = res.get("data",{}).get("Get",{}).get("RunbookChunk",[]) or []
    return [d["text"] for d in data]
