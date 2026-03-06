from typing import TypedDict, List
from langgraph.graph import StateGraph, END

from agents.planner import planner_node
from agents.researcher import research_node
from agents.synthesizer import synthesize_node
from agents.refiner import refiner_node
from env_utils import get_api_key

from langchain_google_genai import ChatGoogleGenerativeAI

class AgentState(TypedDict):
    topic: str
    queries: List[str]
    urls: List[str]
    raw_content: List[str]
    summaries: List[str]
    draft_article: str
    final_article: str

def _get_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        temperature=0.3,
        api_key=get_api_key()
    )

def summarize_node(state):
    llm = _get_llm()
    summaries = []
    raw_docs = [doc for doc in state["raw_content"] if isinstance(doc, str) and doc.strip()]

    if not raw_docs:
        return {"summaries": []}

    for doc in raw_docs:
        summary = llm.invoke(f"Summarize key insights:\n{doc}")
        content = getattr(summary, "content", "")
        if isinstance(content, str) and content.strip():
            summaries.append(content)

    return {"summaries": summaries}


workflow = StateGraph(AgentState)

workflow.add_node("planner", planner_node)
workflow.add_node("research", research_node)
workflow.add_node("summarize", summarize_node)
workflow.add_node("synthesize", synthesize_node)
workflow.add_node("refine", refiner_node)

workflow.set_entry_point("planner")

workflow.add_edge("planner", "research")
workflow.add_edge("research", "summarize")
workflow.add_edge("summarize", "synthesize")
workflow.add_edge("synthesize", "refine")
workflow.add_edge("refine", END)

app = workflow.compile()