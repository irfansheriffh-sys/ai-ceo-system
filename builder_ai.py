from llm import call_llm

def builder_ai(rd_output: dict) -> dict:
    prompt = f'''
    You are a Builder AI in a software company.
    Using the R&D output, generate build details.
    R&D Output:
    {rd_output}
    '''

    response = call_llm(prompt)

    return {
        'project_structure': ['frontend/', 'backend/', 'database/'],
        'frontend_sample': '<div>Frontend UI</div>',
        'raw_response': response
    }
