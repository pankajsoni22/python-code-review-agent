from langgraph.graph import START, END, StateGraph

from code_review_agent.graph.nodes import (
    code_analyzer_node,
    bug_reviewer_node,
    performance_reviewer_node,
    security_reviewer_node
)
from code_review_agent.graph.aggregator import (
    report_aggregator_node
)
from code_review_agent.graph.state import ReviewState

def build_review_graph():

    # Initialize graph builder with default state
    builder = StateGraph(ReviewState)

    # START --> code_reivew_node --> END
    builder.add_node("code_analyzer", code_analyzer_node)
    builder.add_node("bug_reviewer", bug_reviewer_node)
    builder.add_node("performance_reviewer", performance_reviewer_node)
    builder.add_node("security_reviewer", security_reviewer_node)
    builder.add_node("report_aggregator", report_aggregator_node)

    # Add edges
    builder.add_edge(START, "code_analyzer")
    builder.add_edge("code_analyzer", "bug_reviewer")
    builder.add_edge("bug_reviewer", "performance_reviewer")
    builder.add_edge("performance_reviewer", "security_reviewer")
    builder.add_edge("security_reviewer", "report_aggregator")
    builder.add_edge("report_aggregator", END)

    # Get graph
    graph = builder.compile()

    return graph
