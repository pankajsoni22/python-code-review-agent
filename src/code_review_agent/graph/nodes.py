from code_review_agent.chains.code_review import build_code_review_chain
from code_review_agent.graph.state import ReviewState

def code_review_node(state: ReviewState):

    chain = build_code_review_chain()

    result = chain.invoke({
        "code": state["code"]
    })

    # A node typically returns a dictionary containing the state updates it wants to make.
    # It doesn't need to return the entire state.
    # LangGraph merges the returned updates into the existing state. For ordinary fields without reducers, a new value replaces the old value.
    return {
        "review_report": result
    }