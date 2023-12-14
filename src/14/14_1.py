from utils import parse_platform_from_input, slide_rocks, calculate_load

platform = parse_platform_from_input("../../Inputs/14")
platform_after_sliding = slide_rocks(platform)
print(calculate_load(platform_after_sliding))