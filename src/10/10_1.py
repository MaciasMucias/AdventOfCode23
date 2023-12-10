from utils import parse_pipes_from_input, get_next_step, find_connected_pipe, move

animal_location, pipe_map = parse_pipes_from_input("../../Inputs/10")
possible_directions, _ = find_connected_pipe(animal_location, pipe_map)
step = possible_directions.pop()

current_location = move(animal_location, step)

pipe_length = 1

while pipe_map[current_location[0]][current_location[1]] != "S":
    step = get_next_step(step, pipe_map[current_location[0]][current_location[1]])
    current_location = move(current_location, step)
    pipe_length += 1

print(pipe_length // 2)
