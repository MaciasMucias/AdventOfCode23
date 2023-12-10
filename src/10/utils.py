from src.utils import load_input


def move(location: tuple[int, int], direction: tuple[int, int]) -> tuple[int, int]:
    return location[0] + direction[0], location[1] + direction[1]


def find_connected_pipe(starting_location: tuple[int, int], pipes: list[str]) -> tuple[int, int]:
    if pipes[starting_location[0]][starting_location[1]+1] in ["-", "7", "J"]:
        return 0, 1
    if pipes[starting_location[0]+1][starting_location[1]] in ["|", "J", "L"]:
        return 1, 0
    if pipes[starting_location[0]][starting_location[1]-1] in ["-", "F", "L"]:
        return 0, -1
    if pipes[starting_location[0]-1][starting_location[1]] in ["|", "F", "7"]:
        print("This shouldn't have been reached")
        return -1, 0


def parse_pipes_from_input(path) -> tuple[tuple[int, int], list[str]]:
    lines = load_input(path)

    animal_coordinates = None
    for ind, line in enumerate(lines):
        if "S" in line:
            animal_coordinates = (ind, line.index("S"))

    return animal_coordinates, lines


def get_next_step(last_move: tuple[int, int], tile: str) -> tuple[int, int]:
    match tile:
        case "|" | "-":
            return last_move
        case "L" | "7":
            return last_move[1], last_move[0]
        case "J" | "F":
            return -last_move[1], -last_move[0]
