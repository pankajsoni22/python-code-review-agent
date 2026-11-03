import ast

from code_review_agent.chains.code_review import build_code_review_chain
from code_review_agent.graph.state import ReviewState
from code_review_agent.agents.reviewers import build_reviewer

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

def code_analyzer_node(state: ReviewState) -> dict:

    code = state["code"]
    try:
        tree = ast.parse(code)

        functions = [
            node.name
            for node in ast.walk(tree)
            if isinstance(node, (ast.FunctionDef,ast.AsyncFunctionDef))
        ]

        classes = [
            node.name
            for node in ast.walk(tree)
            if isinstance(node, ast.ClassDef)
        ]

        imports = [
            node.names[0].name
            for node in ast.walk(tree)
            if isinstance(node, (ast.Import, ast.ImportFrom)) and node.names
        ]

        context = (
            f"Functions: {functions}\n",
            f"Classes: {classes}\n",
            f"Imports: {imports}\n",
            f"Source lines: {len(code.splitlines())}"
        )
    except Exception as e:
        context = f"Python syntax error: {exec}"

    return {
        "analysis_context": context
    }

def bug_reviewer_node(state: ReviewState) -> dict:

    chain = build_reviewer(
        category="bug detection",
        instructions=(
            "Identify logical errors, edge cases, "
            "incorrect conditions and runtime failures."
        ),
    )

    result = chain.invoke(
        {
            "code": state["code"],
            "analysis_context": state["analysis_context"],
            "category": "bug detection",
            "instructions": (
                "Identify logical errors and runtime failures."
            ),
        }
    )

    return {
        "bug_findings": result.findings
    }


def performance_reviewer_node(state: ReviewState) -> dict:

    chain = build_reviewer(
        category="performance",
        instructions=(
            "Identify inefficient algorithms, unnecessary "
            "computations and memory overhead."
        ),
    )

    result = chain.invoke(
        {
            "code": state["code"],
            "analysis_context": state["analysis_context"],
            "category": "performance",
            "instructions": (
                "Identify computational and memory inefficiencies."
            ),
        }
    )

    return {
        "performance_findings": result.findings
    }


def security_reviewer_node(state: ReviewState) -> dict:

    chain = build_reviewer(
        category="security",
        instructions=(
            "Identify security vulnerabilities, injection "
            "risks, unsafe execution and insecure data handling."
        ),
    )

    result = chain.invoke(
        {
            "code": state["code"],
            "analysis_context": state["analysis_context"],
            "category": "security",
            "instructions": (
                "Focus on security vulnerabilities."
            ),
        }
    )

    return {
        "security_findings": result.findings
    }
