from functools import cache
from src.utils import load_input


def parse_spring_set(line: str) -> tuple[str, tuple[int, ...]]:
    springs_array, numbers_raw = line.split()
    numbers = tuple(map(int, numbers_raw.split(',')))
    return springs_array, numbers


def parse_springs_from_input(path):
    lines = load_input(path)
    return list(map(parse_spring_set, lines))


@cache
def number_of_solutions(springs_array: str, sizes: tuple[int, ...], num_in_group=0):
    if not springs_array:
        return not sizes and not num_in_group

    solutions = 0
    possible = [".", "#"] if springs_array[0] == "?" else springs_array[0]

    for c in possible:
        if c == "#":
            solutions += number_of_solutions(springs_array[1:], sizes, num_in_group+1)
        else:
            if num_in_group:
                if sizes and sizes[0] == num_in_group:
                    solutions += number_of_solutions(springs_array[1:], sizes[1:])
            else:
                solutions += number_of_solutions(springs_array[1:], sizes)
    return solutions
