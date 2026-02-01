from llm import call_llm

def fixer_ai(test_report: dict, build_output: dict) -> dict:
    """
    Fixer AI:
    - Fixes issues reported by Tester AI
    - Improves code and structure
    """

    prompt = f"""
You are a Fixer AI in a software company.

Issues found by Tester AI:
{test_report}

Original Build Output:
{build_output}

Provide fixes and improvements.
"""

    response = call_llm(prompt)

    return {
        "fixes_applied": [
            "Added input validation",
            "Added basic error handling",
            "Improved code structure"
        ],
        "improved_backend_sample": "def main():\\n    try:\\n        print('Backend running safely')\\n    except Exception as e:\\n        print(e)",
        "raw_response": response
    }
