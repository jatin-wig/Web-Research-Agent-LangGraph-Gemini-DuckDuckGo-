from langchain_google_genai import ChatGoogleGenerativeAI
from env_utils import get_api_key


def _get_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        temperature=0.3,
        api_key=get_api_key()
    )

def planner_node(state):
    llm = _get_llm()

    prompt = f"""
    Generate 6 deep research queries for the topic:
    {state['topic']}

    Cover:
    - Latest developments
    - Statistics
    - Case studies
    - Risks
    - Future outlook
    """

    response = llm.invoke(prompt)

    queries = [
        q.strip("- ").strip()
        for q in response.content.split("\n")
        if q.strip()
    ]

    return {"queries": queries}