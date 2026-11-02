from langchain_groq import ChatGroq
from code_review_agent.config.settings import settings

def get_chat_model() -> ChatGroq:
    """
    Initialize and return the configured Groq chat model.
    """

    return ChatGroq(
        model=settings.llm_model,
        temperature=settings.llm_temperature,
        api_key=settings.groq_api_key.get_secret_value(),
    )