from code_review_agent.config.settings import settings
from langchain_core.messages import (
    SystemMessage,
    HumanMessage
)

from code_review_agent.chains.code_review import build_code_review_chain

def main() -> None:
    chain = build_code_review_chain()
    python_code = """
    def calculate_average(numbers: list[float]) -> float:
        if not numbers:
            raise ValueError("Numbers cannot be empty")

        return sum(numbers) / len(numbers)
    """
    

    response = chain.invoke(
        {
            "code": python_code
        }
    )
    print(response.model_dump_json(indent=2))

if __name__ == "__main__":
    main()
