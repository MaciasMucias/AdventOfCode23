from src.utils import Vector, Point
from utils import parse_elements_from_input, calculate_energized_elements, Directions

map_of_elements = parse_elements_from_input("../../Inputs/16")

print(calculate_energized_elements(map_of_elements, Vector(Point(0, -1), Directions.RIGHT)))
