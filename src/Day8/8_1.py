import itertools

from utils import parse_maps_from_input


steps, node_map = parse_maps_from_input("../../Inputs/8")

current_node = "AAA"
destination_node = "ZZZ"

moves_made = 0
steps_cycle = itertools.cycle(steps)

while current_node != destination_node:
    current_moves = node_map.get(current_node)
    current_node = current_moves[next(steps_cycle)]
    moves_made += 1

print(moves_made)
