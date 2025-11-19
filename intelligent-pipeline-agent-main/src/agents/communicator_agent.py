
def render_report(pid: int, health: dict, analysis: dict, plan: dict) -> str:
    return f"Pipeline {pid}\nStatus: {health.get('status')} (score {health.get('health_score')})\nHypothesis: {analysis.get('hypothesis')}\nActions:\n- " + "\n- ".join(plan.get("actions",[]))
