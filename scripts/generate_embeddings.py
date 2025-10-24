
from src.rag.document_loader import load_markdown
from src.rag.retriever import index_runbooks
docs = load_markdown("data/runbooks")
index_runbooks(docs)
print("Indexed runbooks")
