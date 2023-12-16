from utils import parse_races_from_input, calculate_record_options


times, distances = parse_races_from_input("../../Inputs/6")


number_of_ways = 1
for time, distance in zip(times, distances):
    number_of_ways *= calculate_record_options(time, distance)

print(number_of_ways)
