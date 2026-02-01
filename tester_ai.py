from llm import call_llm

def tester_ai(build_output: dict) -> dict:
    """
    Tester AI:
    Reviews build output and finds issues.
    """

    prompt = f"""
You are a Tester AI in a software company.

Analyze the following build output and identify issues.

Build Output:
{build_output}
"""

    response = call_llm(prompt)

    return {
        "issues": [
            "No input validation",
            "No error handling",
            "No authentication checks"
        ],
        "severity": "Medium",
        "raw_response": response
    }
