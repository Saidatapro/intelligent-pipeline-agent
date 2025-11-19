# 🎮 Interactive Demo Guide

## 🌐 Open These URLs in Your Browser

### 1. **Swagger API Documentation** (Recommended!)
```
http://localhost:8000/docs
```

**What you can do:**
- ✅ See all available endpoints
- ✅ Try API calls directly in browser
- ✅ View request/response schemas
- ✅ Test authentication
- ✅ No command line needed!

**Try these endpoints:**
1. Click on `GET /healthz` → Click "Try it out" → Click "Execute"
2. Click on `POST /api/v1/pipelines` → Add API key: `changeme` → Execute
3. Click on `GET /api/v1/pipelines/{pid}/health` → Enter pipeline ID → Execute
4. Click on `POST /api/v1/agents/trigger` → Set parameters → Execute

---

### 2. **Streamlit Dashboard**
```
http://localhost:8501
```

**What you can do:**
- ✅ View all pipeline health scores
- ✅ Trigger agent workflows with UI
- ✅ Toggle approval checkbox
- ✅ See real-time updates

**How to use:**
1. Go to "Overview" tab → See pipeline health cards
2. Go to "Agent" tab → Select pipeline ID
3. Check "Approve critical actions" if needed
4. Click "Trigger Agents" button
5. View JSON response

---

### 3. **Alternative API Documentation**
```
http://localhost:8000/redoc
```

**What you can do:**
- ✅ Alternative API documentation view
- ✅ Better for reading/understanding
- ✅ Cleaner layout

---

## 🧪 Quick Tests You Can Run

### Test 1: Create Your Own Pipeline
```bash
curl -X POST 'http://localhost:8000/api/v1/pipelines' \
  -H 'x-api-key: changeme' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "my_custom_pipeline",
    "source": "postgresql",
    "destination": "snowflake"
  }'
```

### Test 2: Trigger Agents for Your Pipeline
```bash
curl -X POST 'http://localhost:8000/api/v1/agents/trigger?pipeline_id=1&approved=true' \
  -H 'x-api-key: changeme' | python3 -m json.tool
```

### Test 3: Check All Pipelines Health
```bash
for i in {1..3}; do
  echo "Pipeline $i:"
  curl -s http://localhost:8000/api/v1/pipelines/$i/health | python3 -m json.tool
  echo ""
done
```

---

## 🎨 Visual Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                    YOU (Human Operator)                     │
└────────────┬────────────────────────────────────────────────┘
             │
             │ (1) Trigger agents via API or Dashboard
             │
             ▼
┌─────────────────────────────────────────────────────────────┐
│              🤖 Multi-Agent System (LangGraph)              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐ │
│  │   Monitor    │───▶│   Analyzer   │───▶│  Optimizer   │ │
│  │    Agent     │    │    Agent     │    │    Agent     │ │
│  └──────────────┘    └──────────────┘    └──────────────┘ │
│         │                   │                    │         │
│         │                   │                    │         │
│         ▼                   ▼                    ▼         │
│  ┌─────────────────────────────────────────────────────┐  │
│  │          Communicator Agent (Report)                │  │
│  └─────────────────────────────────────────────────────┘  │
│                           │                                │
└───────────────────────────┼────────────────────────────────┘
                            │
                            │ (2) Returns analysis & recommendations
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                    JSON Response                            │
│  {                                                          │
│    "pipeline_id": 1,                                        │
│    "severity": "high",                                      │
│    "analysis": { "hypothesis": "..." },                    │
│    "plan": { "actions": [...] },                           │
│    "report": "..."                                          │
│  }                                                          │
└─────────────────────────────────────────────────────────────┘
```

---

## 📊 What Each Agent Does

### 🔍 Monitor Agent
- Queries database for last 10 metrics
- Calculates average duration, errors, memory, records
- Computes health score (0-100)
- Sets severity: "high" if score < 60, else "low"

### 🧠 Analyzer Agent
- Performs RAG search for similar issues
- Generates root cause hypothesis
- Records incident in database
- Returns relevant context

### ⚙️ Optimizer Agent
- Suggests optimization actions based on analysis
- Marks safe auto-actions (can run without approval)
- Creates recommendations in database
- Returns action plan

### 📢 Communicator Agent
- Formats all findings into human-readable report
- Includes status, hypothesis, and actions
- Returns final state to user

---

## 🎯 Try This Now!

1. **Open Swagger UI**: http://localhost:8000/docs
2. **Scroll to** `POST /api/v1/agents/trigger`
3. **Click** "Try it out"
4. **Set parameters**:
   - `pipeline_id`: 1
   - `approved`: false
5. **Add header**: `x-api-key`: changeme
6. **Click** "Execute"
7. **See the magic happen!** ✨

---

## 🎬 Expected Result

You should see a JSON response like:

```json
{
  "pipeline_id": 1,
  "health": {
    "status": "unknown",
    "health_score": 0.0,
    "metrics": {}
  },
  "analysis": {
    "contexts": [],
    "hypothesis": "Possible resource saturation or schema drift."
  },
  "plan": {
    "actions": [
      "Enable exponential backoff (max 5 retries)",
      "Increase parallelism by +1 worker",
      "Run schema migration & backfill 1h"
    ],
    "auto_safe": [
      "Enable exponential backoff (max 5 retries)"
    ]
  },
  "severity": "high",
  "report": "Pipeline 1\nStatus: unknown (score 0.0)\nHypothesis: Possible resource saturation or schema drift.\nActions:\n- Enable exponential backoff (max 5 retries)\n- Increase parallelism by +1 worker\n- Run schema migration & backfill 1h",
  "approved": false
}
```

---

## 🎉 Congratulations!

You've just witnessed an AI-powered multi-agent system:
- ✅ Automatically analyzing pipeline health
- ✅ Diagnosing root causes
- ✅ Suggesting optimizations
- ✅ Generating human-readable reports
- ✅ All orchestrated by LangGraph!

