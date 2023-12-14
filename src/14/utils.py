import copy

from src.utils import load_input, list_of_strings_to_list_of_lists


def parse_platform_from_input(path):
    lines = load_input(path)
    return list_of_strings_to_list_of_lists(lines)


def slide_rocks(platform: list[list[str]]) -> list[list[str]]:
    platform_copy = copy.deepcopy(platform)
    slide_limit = [0] * len(platform[0])
    for ind_y, row in enumerate(platform_copy):
        for ind_x, val in enumerate(row):
            if val == "O" and slide_limit[ind_x] <= ind_y:
                platform_copy[ind_y][ind_x] = "."
                platform_copy[slide_limit[ind_x]][ind_x] = "O"
                slide_limit[ind_x] += 1
            elif val == "#":
                slide_limit[ind_x] = ind_y + 1
    return platform_copy


def calculate_load(platform: list[list[str]]):
    total_load = 0
    for ind_y, row in enumerate(platform):
        rounded_rocks_in_row = row.count("O")
        load = rounded_rocks_in_row * (len(platform) - ind_y)
        total_load += load

    return total_load
