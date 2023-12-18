from src.utils import load_input, Directions, Direction, Point

DIRECTIONS = {
    "R": Directions.RIGHT,
    "L": Directions.LEFT,
    "U": Directions.UP,
    "D": Directions.DOWN
}


def parse_digging_instructions_from_input(path) -> list[tuple[Direction, int, str]]:
    lines = load_input(path)
    instructions = []
    for line in lines:
        raw_direction, raw_length, raw_color = line.split(" ")
        instructions.append((DIRECTIONS[raw_direction], int(raw_length), raw_color))
    return instructions


def convert_instruction_to_vertex(instruction: tuple[Direction, int, str], previous_vertex) -> tuple[Point, str]:
    direction, length, color = instruction
    vertex = previous_vertex[0]
    return Point(vertex.y + direction.dy * length, vertex.x + direction.dx * length), color


def shoelace_formula(vertices):
    n = len(vertices)
    area = 0

    for i in range(n - 1):
        area += vertices[i][0] * vertices[i + 1][1]
        area -= vertices[i + 1][0] * vertices[i][1]

    # Add the last term
    area += vertices[-1][0] * vertices[0][1]
    area -= vertices[0][0] * vertices[-1][1]

    area = abs(area) / 2.0
    return area
