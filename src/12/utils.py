from src.utils import load_input


def parse_spring_set(line: str) -> tuple[str, tuple[int, ...]]:
    springs_array, numbers_raw = line.split()
    numbers = tuple(map(int, numbers_raw.split(',')))
    return springs_array, numbers


def parse_springs_from_input(path):
    lines = load_input(path)
    return list(map(parse_spring_set, lines))


