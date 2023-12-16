from src.utils import move, Vector, Point
from utils import parse_elements_from_input, count_all_energized_elements, DIRECTIONS

map_of_elements = parse_elements_from_input("../../Inputs/16")

h, w = len(map_of_elements), len(map_of_elements[0])

queue = [Vector(Point(0, -1), DIRECTIONS["RIGHT"])]


while queue:
    vector = queue.pop(0)
    next_point = move(vector.point, vector.direction)

    if not (0 <= next_point.y < h and 0 <= next_point.x < w):
        continue

    element = map_of_elements[next_point.y][next_point.x]

    propagated_light = element.propagate_light(vector.direction)

    for direction in propagated_light:
        queue.append(Vector(next_point, direction))


print(count_all_energized_elements(map_of_elements))
