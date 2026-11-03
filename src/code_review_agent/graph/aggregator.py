from code_review_agent.graph.state import ReviewState
from code_review_agent.schemas.review import ReviewReport

def report_aggregator_node(state: ReviewState) -> dict:

    findings = (
        state["bug_findings"]
        + state["performance_findings"]
        + state["security_findings"]
    )

    if any(f.severity == "critical" for f in findings):
        assessment = "rejected"
    elif findings:
        assessment = "needs_improvement"
    else:
        assessment = "approved"

    report = ReviewReport(
        summary = f"Code review identified {len(findings)} findings.",
        findings=findings,
        overall_assessment=assessment
    )

    return {
        "review_report": report
    }