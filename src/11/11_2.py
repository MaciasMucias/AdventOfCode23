import itertools

from utils import parse_galaxy_from_input, manhattan_distance

EXPANSION_FACTOR = 1000000

adjusted_expansion_factor = EXPANSION_FACTOR - 1

stars, (vertical_expansions, horizontal_expansions) = parse_galaxy_from_input("../../Inputs/11")

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

print(shortest_paths_total)
