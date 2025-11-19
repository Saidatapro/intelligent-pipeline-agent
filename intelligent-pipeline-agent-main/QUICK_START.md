# Quick Start Guide - Intelligent Pipeline Agent

## 🚀 Services Running

| Service | URL | Status |
|---------|-----|--------|
| FastAPI API | http://localhost:8000 | ✅ Running |
| API Documentation | http://localhost:8000/docs | ✅ Available |
| Streamlit Dashboard | http://localhost:8501 | ✅ Running |
| Prometheus Metrics | http://localhost:8000/api/v1/metrics | ✅ Exporting |

## 📝 Quick API Examples

### 1. Health Check
```bash
curl http://localhost:8000/healthz
```

### 2. Create Pipeline
```bash
curl -X POST 'http://localhost:8000/api/v1/pipelines' \
  -H 'x-api-key: changeme' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "etl_orders",
    "source": "s3",
    "destination": "warehouse"
  }'
```

### 3. Check Pipeline Health
```bash
curl http://localhost:8000/api/v1/pipelines/1/health
```

### 4. Trigger Agent Workflow
```bash
# Without approval (will stop before critical actions)
curl -X POST 'http://localhost:8000/api/v1/agents/trigger?pipeline_id=1&approved=false' \
  -H 'x-api-key: changeme'

# With approval (will execute all actions)
curl -X POST 'http://localhost:8000/api/v1/agents/trigger?pipeline_id=1&approved=true' \
  -H 'x-api-key: changeme'
```

## 🎯 What Works

✅ **Multi-Agent Orchestration** - LangGraph workflow with 4 agents  
✅ **Pipeline Health Monitoring** - Real-time health score calculation  
✅ **Root Cause Analysis** - RAG-ready (mocked for local deployment)  
✅ **Optimization Recommendations** - Automated action suggestions  
✅ **Human-in-the-Loop** - Approval workflow for critical actions  
✅ **Prometheus Metrics** - Full metrics export  
✅ **REST API** - All endpoints functional  
✅ **Streamlit Dashboard** - Interactive UI  

## ⚠️ Known Limitations (Local Mode)

- **Weaviate**: Mocked (no real vector search)
- **Redis**: Not running (no caching)
- **MLflow**: Not running (no experiment tracking)
- **Grafana**: Not running (no dashboards)
- **OpenAI**: Dummy key (update in .env for LLM features)

## 🔧 Configuration

Edit `.env` file to customize:
```bash
OPENAI_API_KEY=sk-your-key-here  # Required for LLM features
API_KEY=changeme                  # API authentication
LOG_LEVEL=INFO                    # Logging level
```

## 📊 Agent Workflow

```
1. Monitor Agent → Checks pipeline health
   ↓
2. Analyzer Agent → Performs root cause analysis (if health_score < 60)
   ↓
3. Optimizer Agent → Suggests optimization actions
   ↓
4. Communicator Agent → Generates report
```

## 🎨 Streamlit Dashboard Features

- **Overview Tab**: View all pipeline health scores
- **Agent Tab**: Trigger agent workflows with approval toggle
- **Knowledge Tab**: RAG system status

## 📦 Files Modified

1. `requirements.txt` - Fixed dependency versions
2. `src/database/session.py` - SQLite instead of PostgreSQL
3. `src/agents/monitor_agent.py` - SQLAlchemy 2.0 compatibility
4. `src/agents/orchestrator.py` - LangGraph configuration fixes
5. `src/rag/vector_store.py` - Mock Weaviate for local testing
6. `.env` - Environment configuration

## 🐛 All Issues Fixed

✅ Dependency conflicts resolved  
✅ Database connection working  
✅ SQLAlchemy 2.0 compatibility  
✅ LangGraph thread_id configuration  
✅ Conditional edges END mapping  
✅ Weaviate connection handling  

## 🎉 Result

**System is fully operational in local mode!** All core functionality works as expected.
