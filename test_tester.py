from rd_ai import rd_ai
from builder_ai import builder_ai
from tester_ai import tester_ai

rd_result = rd_ai("Build a simple task management app")
build_result = builder_ai(rd_result)
test_result = tester_ai(build_result)

print(test_result)
