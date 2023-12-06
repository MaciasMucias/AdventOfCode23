from utils import parse_races_from_input_bad_kerning, calculate_record_options


time, distance = parse_races_from_input_bad_kerning("../../Inputs/6")


number_of_ways = calculate_record_options(time, distance)

print(number_of_ways)
