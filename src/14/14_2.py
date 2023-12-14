from utils import parse_platform_from_input, slide_rocks, calculate_load, rotate_tuple_90


def full_cycle(platform):
    for _ in range(4):
        platform = slide_rocks(platform)
        platform = rotate_tuple_90(platform)
    return platform


platform = parse_platform_from_input("../../Inputs/14")
platform = tuple(map(tuple, platform))
before_last_spin = platform

cache = {}

num_of_iterations = 1_000_000_000
ended = False
for ind in range(num_of_iterations):
    platform = full_cycle(platform)
    if platform in cache:
        last_seen = cache[platform]
        loop_size = ind - last_seen
        for _ in range((num_of_iterations-ind-1) % loop_size):
            platform = full_cycle(platform)
        break
    cache[platform] = ind

print(calculate_load(platform))
