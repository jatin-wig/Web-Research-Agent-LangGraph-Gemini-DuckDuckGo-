import streamlit as st
from env_utils import configure_api_env, get_api_key

configure_api_env()

st.set_page_config(
    page_title="Gemini Autonomous Research Agent",
    layout="wide"
)

st.title("Web Researcher by LangGraph")

with st.sidebar:
    st.header("Settings")
    st.info("LLM: Gemini 2.5 Flash Lite")
    try:
        get_api_key()
        st.success("Gemini API key detected")
    except RuntimeError:
        st.error("Gemini API key missing")
    st.markdown("---")
    st.caption("Multi-Agent + LangGraph")

try:
    from graph import app
except Exception as exc:
    st.error(f"Startup error: {exc}")
    st.stop()

topic = st.text_input("Enter Research Topic")

if st.button("Generate Article"):

    if not topic.strip():
        st.warning("Please enter a research topic.")
        st.stop()

    with st.spinner("Conducting deep research across the web..."):
        result = app.invoke({
            "topic": topic,
            "queries": [],
            "urls": [],
            "raw_content": [],
            "summaries": [],
            "draft_article": "",
            "final_article": ""
        })

    st.success("Article Generated Successfully!")

    st.markdown("## Final Article")
    st.markdown(result["final_article"])

    with st.expander("Sources Used"):
        for url in result["urls"]:
            st.write(url)