from rd_ai import rd_ai
from builder_ai import builder_ai
from tester_ai import tester_ai
from fixer_ai import fixer_ai

rd_result = rd_ai("Build a simple task management app")
build_result = builder_ai(rd_result)
test_result = tester_ai(build_result)
fix_result = fixer_ai(test_result, build_result)

print(fix_result)
