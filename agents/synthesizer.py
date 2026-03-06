from langchain_google_genai import ChatGoogleGenerativeAI
from env_utils import get_api_key


def _get_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        temperature=0.4,
        api_key=get_api_key()
    )

def synthesize_node(state):
    llm = _get_llm()
    combined = "\n\n".join(state["summaries"])

    prompt = f"""
    Write a professional, publication-grade article about:
    {state['topic']}

    Requirements:
    - Strong introduction
    - Structured H2 and H3 headings
    - Data-backed analysis
    - Real-world examples
    - Clear conclusion

    Research material:
    {combined}
    """

    draft = llm.invoke(prompt)

    return {"draft_article": draft.content}