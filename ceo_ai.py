from rd_ai import rd_ai
from builder_ai import builder_ai
from tester_ai import tester_ai
from fixer_ai import fixer_ai

def ceo_ai(client_request: str) -> dict:
    logs = []

    logs.append('CEO AI: Received client request')

    logs.append('CEO AI: Assigning task to R&D AI')
    rd_output = rd_ai(client_request)

    logs.append('CEO AI: Assigning task to Builder AI')
    build_output = builder_ai(rd_output)

    logs.append('CEO AI: Assigning task to Tester AI')
    test_output = tester_ai(build_output)

    logs.append('CEO AI: Assigning task to Fixer AI')
    fix_output = fixer_ai(test_output, build_output)

    logs.append('CEO AI: Project workflow completed')

    return {
        'logs': logs,
        'rd_output': rd_output,
        'build_output': build_output,
        'test_output': test_output,
        'fix_output': fix_output
    }
