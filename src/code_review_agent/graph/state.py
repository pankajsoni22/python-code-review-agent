from typing import TypedDict
from code_review_agent.schemas.review import ReviewReport

class ReviewState(TypedDict):
    code: str
    review_report: ReviewReport | None