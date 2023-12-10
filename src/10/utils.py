from src.utils import load_input


def move(location: tuple[int, int], direction: tuple[int, int]) -> tuple[int, int]:
    return location[0] + direction[0], location[1] + direction[1]


def get_pipe_directions(pipe_element: str) -> set[tuple[int, int]]:
    if pipe_element == "-":
        return {(0, -1), (0, 1)}
    if pipe_element == "|":
        return {(-1, 0), (1, 0)}
    if pipe_element == "L":
        return {(-1, 0), (0, 1)}
    if pipe_element == "F":
        return {(1, 0), (0, 1)}
    if pipe_element == "7":
        return {(1, 0), (0, -1)}
    if pipe_element == "J":
        return {(-1, 0), (0, -1)}


def find_connected_pipe(location: tuple[int, int], pipe_map: list[list[str]]) -> tuple[set[tuple[int, int]], str]:
    pipe_element = pipe_map[location[0]][location[1]]
    if pipe_element != "S":
        return get_pipe_directions(pipe_element), pipe_element

    # Need to deduce the correct piece
    moving_right, moving_down, moving_left, moving_up = {(0, 1)}, {(1, 0)}, {(0, -1)}, {(-1, 0)}
    connecting_pipes = set()
    if pipe_map[location[0]][location[1] + 1] in ["-", "7", "J"]:
        connecting_pipes.add((0, 1))
    if pipe_map[location[0] + 1][location[1]] in ["|", "J", "L"]:
        connecting_pipes.add((1, 0))
    if pipe_map[location[0]][location[1] - 1] in ["-", "F", "L"]:
        connecting_pipes.add((0, -1))
    if pipe_map[location[0] - 1][location[1]] in ["|", "F", "7"]:
        connecting_pipes.add((-1, 0))

    if connecting_pipes == moving_up | moving_down:
        return connecting_pipes, "|"
    if connecting_pipes == moving_up | moving_right:
        return connecting_pipes, "L"
    if connecting_pipes == moving_up | moving_left:
        return connecting_pipes, "J"
    if connecting_pipes == moving_right | moving_left:
        return connecting_pipes, "-"
    if connecting_pipes == moving_right | moving_down:
        return connecting_pipes, "F"
    if connecting_pipes == moving_left | moving_down:
        return connecting_pipes, "7"


def parse_pipes_from_input(path) -> tuple[tuple[int, int], list[list[str]]]:
    lines = load_input(path)

    animal_coordinates = None
    for ind, line in enumerate(lines):
        if "S" in line:
            animal_coordinates = (ind, line.index("S"))

    return animal_coordinates, list(map(list, lines))


def get_next_step(last_move: tuple[int, int], tile: str) -> tuple[int, int]:
    match tile:
        case "|" | "-":
            return last_move
        case "L" | "7":
            return last_move[1], last_move[0]
        case "J" | "F":
            return -last_move[1], -last_move[0]


def connect_bends(bend1: tuple[int, int], bend2: tuple[int, int], pipe_map: list[list[str]]):
    direction = (bend2[0] - bend1[0], bend2[1] - bend1[1])
    if direction[0]:
        connector = "|"
        move_count = abs(direction[0])
    else:
        connector = "-"
        move_count = abs(direction[1])

    direction = (direction[0] // move_count, direction[1] // move_count)

    for i in range(move_count - 1):
        bend1 = move(bend1, direction)
        pipe_map[bend1[0]][bend1[1]] = connector


def flood_fill(location: tuple[int, int], pipe_map: list[list[str]]):
    if pipe_map[location[0]][location[1]] != '.':
        return
    pipe_map[location[0]][location[1]] = "i"
    flood_fill(move(location, (0, 1)), pipe_map)
    flood_fill(move(location, (1, 0)), pipe_map)
    flood_fill(move(location, (0, -1)), pipe_map)
    flood_fill(move(location, (-1, 0)), pipe_map)


def mark_tile(pipe: tuple[str, tuple[int, int]], parity: int, pipe_map: list[list[str]]):
    tile, location = pipe
    match tile:
        case "L":
            mark_offset = (-1, 1)
        case "F":
            mark_offset = (1, 1)
        case "7":
            mark_offset = (1, -1)
        case "J":
            mark_offset = (-1, -1)
        case _:
            raise ValueError(f"Invalid bend: {tile}")
    if parity == 1:
        mark_location = move(location, mark_offset)
        if pipe_map[mark_location[0]][mark_location[1]] == ".":
            flood_fill(mark_location, pipe_map)
    else:
        mark_offsets = [(-mark_offset[0], 0), (-mark_offset[0], -mark_offset[1]), (0, -mark_offset[1])]
        for mark_offset in mark_offsets:
            mark_location = move(location, mark_offset)
            if pipe_map[mark_location[0]][mark_location[1]] == ".":
                flood_fill(mark_location, pipe_map)
