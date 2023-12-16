import itertools
import collections

from utils import parse_pipes_from_input, get_next_step, find_connected_pipe, connect_bends, get_pipe_directions, \
    mark_tile
from src.utils import move

animal_location, pipe_map = parse_pipes_from_input("../../Inputs/10")
possible_directions, pipe_shape = find_connected_pipe(animal_location, pipe_map)
step = possible_directions.pop()

current_location = move(animal_location, step)

if pipe_shape in "LJ7F":
    bends = [(pipe_shape, animal_location)]
else:
    bends = []

while pipe_map[current_location[0]][current_location[1]] != "S":
    step = get_next_step(step, pipe_map[current_location[0]][current_location[1]])
    current_location = move(current_location, step)
    if pipe_map[current_location[0]][current_location[1]] in "LJ7F":
        bends.append((pipe_map[current_location[0]][current_location[1]], current_location))

new_map = [["."] * len(pipe_map[0]) for _ in range(len(pipe_map))]

bend_loop = itertools.cycle(bends)
bend = next(bend_loop)
for ind in range(len(bends) + 1):
    next_bend = next(bend_loop)
    new_map[bend[1][0]][bend[1][1]] = bend[0]
    connect_bends(bend[1], next_bend[1], new_map)
    bend = next_bend

parity = 1
current_bend = None

for ind, row in enumerate(new_map):
    if "F" in row:
        current_bend = (ind, row.index("F"))
        break

starting_spot = bends.index(("F", current_bend))

bend_loop = collections.deque(bends)
bend_loop.rotate(-starting_spot)

prev_bend = bend_loop[-1]

for i in range(len(bends)):
    bend = bend_loop[0]

    if not get_pipe_directions(bend[0]) & get_pipe_directions(prev_bend[0]):
        parity *= -1

    mark_tile(bend, parity, new_map)

    prev_bend = bend
    bend_loop.rotate(-1)

inside_count = 0

for row in new_map:
    inside_count += row.count("i")

print(inside_count)
