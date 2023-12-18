from src.utils import Point
from utils import parse_digging_instructions_from_input, convert_color_to_instruction, convert_instruction_to_vertex, shoelace_formula

instructions = parse_digging_instructions_from_input('../../Inputs/18')

all_vertices = [(Point(0, 0), None)]
naive_circumference = 0
for instruction in instructions:
    instruction = convert_color_to_instruction(instruction)
    naive_circumference += instruction[1]
    vertex = convert_instruction_to_vertex(instruction, all_vertices[-1])
    all_vertices.append(vertex)


for i in range(len(all_vertices)):
    all_vertices[i] = all_vertices[i][0]

print(shoelace_formula(all_vertices) + naive_circumference / 2 + 1)