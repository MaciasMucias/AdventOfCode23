import itertools
import math

from utils import parse_maps_from_input, get_every_ghost_starting_place, is_end_space


steps, node_map = parse_maps_from_input("../../Inputs/8")

starting_nodes = get_every_ghost_starting_place(node_map)
moves_made = [0] * len(starting_nodes)

for ind, node in enumerate(starting_nodes):
    steps_cycle = itertools.cycle(steps)
    while not is_end_space(node):
        current_moves = node_map.get(node)
        node = current_moves[next(steps_cycle)]
        moves_made[ind] += 1

print(math.lcm(*moves_made))
