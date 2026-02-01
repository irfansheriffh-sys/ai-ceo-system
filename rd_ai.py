from llm import call_llm

def rd_ai(requirements: str) -> dict:
    """
    R&D AI:
    - Analyzes requirements
    - Suggests features
    - Recommends tech stack
    - Identifies risks
    """

    prompt = f"""
You are an R&D AI in a software company.

Analyze the following project requirements and provide:
1. Key features
2. Recommended tech stack
3. Possible risks

Project Requirements:
{requirements}
"""

    response = call_llm(prompt)

    return {
        "features": [
            "User authentication",
            "Dashboard",
            "Core CRUD functionality"
        ],
        "tech_stack": {
            "frontend": "React",
            "backend": "FastAPI",
            "database": "PostgreSQL"
        },
        "risks": [
            "Limited development time",
            "Scalability considerations"
        ],
        "raw_response": response
    }
