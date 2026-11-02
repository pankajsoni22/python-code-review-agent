from langchain_core.runnables import Runnable

from code_review_agent.llm.client import get_chat_model
from code_review_agent.prompts.code_review import CODE_REVIEW_PROMPT
from code_review_agent.schemas.review import ReviewReport

def build_code_review_chain() -> Runnable:

    llm = get_chat_model()

    structured_llm = llm.with_structured_output(ReviewReport)

    chain = CODE_REVIEW_PROMPT | structured_llm # LCEL -> LangChain Expression Language

    return chain