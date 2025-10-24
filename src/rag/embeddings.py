
from typing import List
from src.utils.config import settings

def embed_texts(texts: List[str]) -> List[List[float]]:
    if settings.llm_provider == "openai" and settings.openai_api_key:
        from openai import OpenAI
        client = OpenAI(api_key=settings.openai_api_key)
        resp = client.embeddings.create(model=settings.openai_embed_model, input=texts)
        return [d.embedding for d in resp.data]
    # fallback toy embedding (for local dev without keys)
    import hashlib
    out=[]
    for t in texts:
        h = hashlib.sha256(t.encode()).digest()
        out.append([b/255 for b in h]*6)  # 192-dim approx
    return out
