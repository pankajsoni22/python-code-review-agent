from code_review_agent.config.settings import settings
from code_review_agent.graph.workflow import build_review_graph

def main() -> None:
    graph = build_review_graph()
    python_code = """
    def find_duplicates(items):
        duplicates = []

        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                if items[i] == items[j] and items[i] not in duplicates:
                    duplicates.append(items[i])

        return duplicates
    """
    initial_state = {
        "code": python_code,
        "analysis_context": None,
        "bug_findings": [],
        "performance_findings": [],
        "security_findings": [],
        "review_report": None,
    }

    response = graph.invoke(initial_state)
    report = response["review_report"]
    print("\nCODE REVIEW REPORT")
    print("==================")

    print(f"\nSummary: {report.summary}")
    print(f"Assessment: {report.overall_assessment}")

    for finding in report.findings:
        print(f"\n[{finding.severity.upper()}] {finding.title}")
        print(f"Category: {finding.category}")
        print(f"Description: {finding.description}")
        print(f"Recommendation: {finding.recommendation}")

    print(response['review_report'])

if __name__ == "__main__":
    main()
