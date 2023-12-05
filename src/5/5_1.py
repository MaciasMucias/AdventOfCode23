from utils import parse_input, get_destination_from_map

almanac_data = parse_input("../../Inputs/5")

seeds, maps = almanac_data


locations = []
for value in seeds:
    source_type = "seed"

    while source_type != "location":
        destination_type, appropriate_map = maps.get(source_type)
        value = get_destination_from_map(value, appropriate_map)
        source_type = destination_type

    locations.append(value)

print(min(locations))
