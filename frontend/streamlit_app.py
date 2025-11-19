
import os, requests, streamlit as st, plotly.graph_objects as go
API=os.getenv("API_BASE","http://api:8000")
st.set_page_config(page_title="IPA", page_icon="🧠", layout="wide")
st.title("🧠 Intelligent Pipeline Agent")
tab1,tab2,tab3=st.tabs(["Overview","Agent","Knowledge"])
with tab1:
    st.subheader("Pipelines")
    cols=st.columns(5)
    for i,c in enumerate(cols, start=1):
        try:
            r=requests.get(f"{API}/api/v1/pipelines/{i}/health",timeout=1.5).json()
            c.metric(f"Pipeline {i}", r["status"], f"score {r['health_score']}")
        except: c.metric(f"Pipeline {i}","unknown","score 0")
with tab2:
    pid=st.number_input("Pipeline ID",1,10,1)
    approved=st.checkbox("Approve critical actions",False)
    if st.button("Trigger Agents"):
        resp=requests.post(f"{API}/api/v1/agents/trigger",params={"pipeline_id":pid,"approved":approved})
        st.json(resp.json())
with tab3:
    st.write("Runbooks indexed; use agents for contextual retrieval.")
