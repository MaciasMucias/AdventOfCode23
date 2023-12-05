from src.utils import paired
from utils import parse_input, get_destination_slices_from_map, combine_slices

almanac_data = parse_input("../../Inputs/5")

seeds, maps = almanac_data

raw_slices = [(start, start+length-1) for start, length in paired(seeds)]
slices = combine_slices(raw_slices)
source_type = "seed"

while source_type != "location":
    destination_type, appropriate_map = maps.get(source_type)
    slices = get_destination_slices_from_map(slices, appropriate_map)
    source_type = destination_type

print(slices[0][0])

