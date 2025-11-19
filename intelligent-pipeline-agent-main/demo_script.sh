#!/bin/bash

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║   🧠 Intelligent Pipeline Agent - Live Demo                   ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}Step 1: Health Check${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
curl -s http://localhost:8000/healthz | python3 -m json.tool
echo ""

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}Step 2: Register Multiple Pipelines${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

echo -e "${YELLOW}→ Creating ETL Orders Pipeline...${NC}"
curl -s -X POST 'http://localhost:8000/api/v1/pipelines' \
  -H 'x-api-key: changeme' \
  -H 'Content-Type: application/json' \
  -d '{"name":"etl_orders","source":"s3","destination":"warehouse"}' | python3 -m json.tool
echo ""

echo -e "${YELLOW}→ Creating Streaming Analytics Pipeline...${NC}"
curl -s -X POST 'http://localhost:8000/api/v1/pipelines' \
  -H 'x-api-key: changeme' \
  -H 'Content-Type: application/json' \
  -d '{"name":"streaming_analytics","source":"kafka","destination":"bigquery"}' | python3 -m json.tool
echo ""

echo -e "${YELLOW}→ Creating Data Lake Sync Pipeline...${NC}"
curl -s -X POST 'http://localhost:8000/api/v1/pipelines' \
  -H 'x-api-key: changeme' \
  -H 'Content-Type: application/json' \
  -d '{"name":"data_lake_sync","source":"postgres","destination":"s3"}' | python3 -m json.tool
echo ""

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}Step 3: Check Pipeline Health${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

for i in 1 2 3; do
  echo -e "${YELLOW}→ Pipeline $i Health:${NC}"
  curl -s http://localhost:8000/api/v1/pipelines/$i/health | python3 -m json.tool
  echo ""
done

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}Step 4: Trigger Multi-Agent Workflow (Without Approval)${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "${YELLOW}→ Running agents for Pipeline 1 (approved=false)...${NC}"
echo ""
curl -s -X POST 'http://localhost:8000/api/v1/agents/trigger?pipeline_id=1&approved=false' \
  -H 'x-api-key: changeme' | python3 -m json.tool
echo ""

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}Step 5: Trigger Multi-Agent Workflow (With Approval)${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "${YELLOW}→ Running agents for Pipeline 2 (approved=true)...${NC}"
echo ""
curl -s -X POST 'http://localhost:8000/api/v1/agents/trigger?pipeline_id=2&approved=true' \
  -H 'x-api-key: changeme' | python3 -m json.tool
echo ""

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}Step 6: View Prometheus Metrics${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
curl -s http://localhost:8000/api/v1/metrics | grep -E "^(# |pipeline_|agent_)" | head -20
echo ""

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✅ Demo Complete!${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "${YELLOW}📊 Access Points:${NC}"
echo "   • API Documentation: http://localhost:8000/docs"
echo "   • Streamlit Dashboard: http://localhost:8501"
echo "   • Metrics Endpoint: http://localhost:8000/api/v1/metrics"
echo ""
echo -e "${YELLOW}🎯 What Just Happened:${NC}"
echo "   1. ✅ Verified system health"
echo "   2. ✅ Created 3 data pipelines"
echo "   3. ✅ Checked pipeline health scores"
echo "   4. ✅ Ran multi-agent workflow WITHOUT approval"
echo "   5. ✅ Ran multi-agent workflow WITH approval (includes report)"
echo "   6. ✅ Viewed Prometheus metrics"
echo ""
echo -e "${YELLOW}🤖 Agent Workflow:${NC}"
echo "   Monitor Agent → Analyzer Agent → Optimizer Agent → Communicator Agent"
echo ""

