from langchain_google_genai import ChatGoogleGenerativeAI
from env_utils import get_api_key


def _get_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        temperature=0.3,
        api_key=get_api_key()
    )

def refiner_node(state):
    llm = _get_llm()
    prompt = f"""
    Improve and polish the article for clarity, depth, structure, and factual consistency.

    Original Article:
    {state['draft_article']}

    Produce a significantly improved final version.
    """

    final = llm.invoke(prompt)

    return {"final_article": final.content}