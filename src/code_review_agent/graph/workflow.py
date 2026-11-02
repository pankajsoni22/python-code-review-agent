from langgraph.graph import START, END, StateGraph

from code_review_agent.graph.nodes import code_review_node
from code_review_agent.graph.state import ReviewState

def build_review_graph():

    # Initialize graph builder with default state
    builder = StateGraph(ReviewState)

    # START --> code_reivew_node --> END
    builder.add_node("code_review", code_review_node)

    # Add edges
    builder.add_edge(START, "code_review")
    builder.add_edge("code_review", END)

    # Get graph
    graph = builder.compile()

    return graph
