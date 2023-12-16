from utils import parse_galaxy_from_input, shortest_path_total

EXPANSION_FACTOR = 2

adjusted_expansion_factor = EXPANSION_FACTOR - 1

stars, (vertical_expansions, horizontal_expansions) = parse_galaxy_from_input("../../Inputs/11")

print(shortest_path_total(stars, vertical_expansions, horizontal_expansions, adjusted_expansion_factor))
