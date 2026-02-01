from rd_ai import rd_ai
from builder_ai import builder_ai

rd_result = rd_ai("Build a simple task management app")
build_result = builder_ai(rd_result)

print(build_result)
