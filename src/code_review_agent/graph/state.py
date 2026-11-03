from typing import TypedDict
from code_review_agent.schemas.review import ReviewReport, ReviewFinding

class ReviewState(TypedDict):
    # Input
    code: str

    # Code analysis
    analysis_context: str | None
    
    # Specialized reviewer
    bug_findings: list[ReviewFinding]
    performance_findings: list[ReviewFinding]
    security_findings: list[ReviewFinding]

    # Final output
    review_report: ReviewReport | None