import copy
from functools import cache
from src.utils import load_input, list_of_strings_to_list_of_lists, columnwise_list


def parse_platform_from_input(path):
    lines = load_input(path)
    platform = list_of_strings_to_list_of_lists(lines)
    return tuple(map(tuple, platform))


@cache
def slide_rocks(platform: tuple[tuple[str]]) -> tuple[tuple[str]]:
    columnwise_platform = columnwise_list(platform)
    platform_after_sliding = []
    for column in columnwise_platform:
        column_after_slide = []
        last_ind = -1
        sliding_rocks_found = 0
        ind = 0
        for ind, val in enumerate(column):
            if val == "#":
                tiles_from_last_ind = ind - last_ind - 1
                column_after_slide.extend(
                    ["O"] * sliding_rocks_found + ["."] * (tiles_from_last_ind - sliding_rocks_found) + ["#"])
                last_ind = ind
                sliding_rocks_found = 0
            elif val == "O":
                sliding_rocks_found += 1
        tiles_from_last_ind = ind - last_ind
        column_after_slide.extend(["O"] * sliding_rocks_found + ["."] * (tiles_from_last_ind - sliding_rocks_found))
        platform_after_sliding.append(tuple(column_after_slide))
    return columnwise_list(tuple(platform_after_sliding))


def calculate_load(platform: tuple[tuple[str], ...]):
    total_load = 0
    for ind_y, row in enumerate(platform):
        rounded_rocks_in_row = row.count("O")
        load = rounded_rocks_in_row * (len(platform) - ind_y)
        total_load += load

    return total_load


def rotate_tuple_90(to_rotate: tuple[tuple, ...]) -> tuple[tuple, ...]:
    return tuple(map(tuple, zip(*reversed(to_rotate))))


def full_cycle(platform):
    for _ in range(4):
        platform = slide_rocks(platform)
        platform = rotate_tuple_90(platform)
    return platform
