from functools import cache
from utils import parse_springs_from_input


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


data = parse_springs_from_input("../../Inputs/12")

all_solutions = 0
for springs, numbers in data:
    all_solutions += number_of_solutions(springs+".", numbers)

print(all_solutions)