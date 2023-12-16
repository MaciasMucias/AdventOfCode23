from src.utils import Vector, Point
from utils import parse_elements_from_input, calculate_energized_elements, Directions

map_of_elements = parse_elements_from_input("../../Inputs/16")

h, w = len(map_of_elements), len(map_of_elements[0])
starting_vectors = []

for i in range(h):
    starting_vectors.append((Vector(Point(i, -1), Directions.RIGHT)))
    starting_vectors.append((Vector(Point(i, w), Directions.LEFT)))

for i in range(w):
    starting_vectors.append((Vector(Point(-1, i), Directions.DOWN)))
    starting_vectors.append((Vector(Point(h, i), Directions.UP)))

max_energy = 0

for vector in starting_vectors:
    energy = calculate_energized_elements(map_of_elements, vector)
    max_energy = max(max_energy, energy)

print(max_energy)
