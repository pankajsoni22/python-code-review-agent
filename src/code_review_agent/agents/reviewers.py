from langchain_core.prompts import ChatPromptTemplate
from code_review_agent.llm.client import get_chat_model
from code_review_agent.schemas.review import ReviewFindings


def build_reviewer(category: str, instructions: str):
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
                You are an expert Python code reviewer.

                Your responsibility is to review Python code
                specifically for: {category}.

                Additional instructions:
                {instructions}

                Return only findings relevant to your review area.

                Do not invent problems.
                If no issues are found, return an empty findings list.

                Assign an appropriate severity and provide
                actionable recommendations.
                """
            ),
            (
                "human",
                """
                Code analysis context:
                {analysis_context}

                Python source code:
                ```python
                {code}
                ```
                """
            ),
        ]
    )

    # fill the partial values, rest of it will fill during chain.invoke
    prompt = prompt.partial(
        category=category,
        instructions=instructions
    )

    llm = get_chat_model()
    structured_llm = llm.with_structured_output(ReviewFindings)

    return prompt | structured_llm