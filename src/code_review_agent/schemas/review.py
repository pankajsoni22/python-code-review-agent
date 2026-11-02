from typing import Literal

from pydantic import BaseModel, Field

class ReviewFinding(BaseModel):
    category: Literal[
        "bug",
        "performance",
        "security",
        "code_quality",
        "concurrency"
    ]

    severity: Literal[
        "critical",
        "high",
        "medium",
        "low",
        "info"
    ]

    title: str = Field(description="Short title of the finding")

    description: str = Field(description="Detailed explanation of the issue")

    recommendation: str = Field(description="Actionable recommendation to fix the issue")

    line_number: int | None = Field(
        default=None,
        description="Relevant source code line number, if identifiable"
    )


class ReviewReport(BaseModel):
    summary: str = Field(description="Overall summary of the code reivew")
    
    findings: list[ReviewFinding] = Field(
        default_factory=list, 
        description="List of identified code review findings"
    )

    overall_assessment: Literal[
        "approved",
        "rejected",
        "needs_improvement",
    ]

    