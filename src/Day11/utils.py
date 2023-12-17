import itertools

from src.utils import load_input, columnwise_list, list_of_strings_to_list_of_lists


def expand_galaxy(galaxy: list[list[str]]) -> tuple[list[int], list[int]]:
    vertical_expansions = []
    for row, line in enumerate(galaxy):
        if "#" not in line:
            vertical_expansions.append(row)

    rotated_galaxy = columnwise_list(galaxy)
    horizontal_expansions = []
    for column, line in enumerate(rotated_galaxy):
        if "#" not in line:
            horizontal_expansions.append(column)

    return vertical_expansions, horizontal_expansions


def locate_stars(galaxy: list[list[str]]) -> dict[int, tuple[int, int]]:
    stars = {}
    star_id = 1
    for y, row in enumerate(galaxy):
        if "#" not in row:
            continue
        for x, char in enumerate(row):
            if char == "#":
                stars[star_id] = (y, x)
                star_id += 1
    return stars


def parse_galaxy_from_input(path) -> tuple[dict[int, tuple[int, int]], tuple[list[int], list[int]]]:
    lines = load_input(path)
    galaxy = list_of_strings_to_list_of_lists(lines)
    stars = locate_stars(galaxy)
    vertical_expansions, horizontal_expansions = expand_galaxy(galaxy)

    return stars, (vertical_expansions, horizontal_expansions)


def manhattan_distance(from_star: tuple[int, int], to_star: tuple[int, int]) -> int:
    return abs(from_star[0] - to_star[0]) + abs(from_star[1] - to_star[1])


def shortest_path_total(stars, vertical_expansions, horizontal_expansions, adjusted_expansion_factor):
    shortest_paths_total = 0

    for star_a, star_b in itertools.combinations(stars.items(), 2):
        name_a, location_a = star_a[0], star_a[1]
        name_b, location_b = star_b[0], star_b[1]

        shortest_paths_total += manhattan_distance(location_a, location_b)
        shortest_paths_total += len(list(
            filter(lambda x: min(location_a[0], location_b[0]) <= x <= max(location_a[0], location_b[0]),
                   vertical_expansions))) * adjusted_expansion_factor
        shortest_paths_total += len(list(
            filter(lambda x: min(location_a[1], location_b[1]) <= x <= max(location_a[1], location_b[1]),
                   horizontal_expansions))) * adjusted_expansion_factor
    return shortest_paths_total
