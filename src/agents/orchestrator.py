
from typing import TypedDict
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from .monitor_agent import compute_health
from .analyzer_agent import analyze
from .optimizer_agent import optimize
from .communicator_agent import render_report
from .tools import record_incident, create_recommendation

class AgentState(TypedDict, total=False):
    pipeline_id: int
    health: dict
    analysis: dict
    plan: dict
    severity: str
    report: str
    approved: bool

def node_monitor(s: AgentState) -> AgentState:
    h = compute_health(s["pipeline_id"]); s["health"]=h
    s["severity"] = "high" if h["health_score"]<60 else "low"
    return s

def node_analyze(s: AgentState) -> AgentState:
    s["analysis"] = analyze(s["pipeline_id"], {"health": s["health"]})
    record_incident(s["pipeline_id"], s["severity"], "Anomaly detected", {"health": s["health"]})
    return s

def node_optimize(s: AgentState) -> AgentState:
    s["plan"] = optimize(s["pipeline_id"], s["analysis"])
    for a in s["plan"]["actions"]:
        create_recommendation(s["pipeline_id"], a, s["analysis"].get("hypothesis",""))
    return s

def node_communicate(s: AgentState) -> AgentState:
    s["report"] = render_report(s["pipeline_id"], s["health"], s["analysis"], s["plan"])
    return s

def after_monitor(s: AgentState):
    return "analyze" if s["severity"]=="high" else "communicate"

def after_optimize(s: AgentState):
    auto = set(s["plan"].get("auto_safe",[]))
    needs = any(a not in auto for a in s["plan"].get("actions",[]))
    return "communicate" if not needs or s.get("approved") else END

def build_graph():
    g = StateGraph(AgentState)
    g.add_node("monitor", node_monitor)
    g.add_node("analyze", node_analyze)
    g.add_node("optimize", node_optimize)
    g.add_node("communicate", node_communicate)
    g.set_entry_point("monitor")
    g.add_conditional_edges("monitor", after_monitor, {"analyze":"analyze","communicate":"communicate"})
    g.add_edge("analyze","optimize")
    g.add_conditional_edges("optimize", after_optimize, {"communicate":"communicate", END: END})
    return g.compile(checkpointer=MemorySaver())

workflow = build_graph()

def run_once(pipeline_id: int, approved: bool=False) -> AgentState:
    return workflow.invoke(
        {"pipeline_id": pipeline_id, "approved": approved},
        config={"configurable": {"thread_id": str(pipeline_id)}}
    )
