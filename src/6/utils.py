import math

from src.utils import load_input


def calculate_record_options(time, distance):
    distance += 1  # the record must be beaten, not tied
    delta = time**2-4*distance
    if delta < 0:
        return 0
    sqrt_delta = math.sqrt(delta)
    lower_bound = math.ceil((time - sqrt_delta)/2)
    lower_bound = max(1, lower_bound)
    higher_bound = math.floor((time + sqrt_delta)/2)
    return higher_bound - lower_bound + 1


def parse_races_from_input(path) -> tuple[list[int], list[int]]:
    lines = load_input(path)
    raw_times, raw_distances = lines
    raw_times = raw_times.replace("  ", " ").replace("\n", "")[6:]
    raw_distances = raw_distances.replace("  ", " ").replace("\n", "")[10:]
    times = list(map(int, raw_times.split()))
    distances = list(map(int, raw_distances.split()))
    return times, distances


def parse_races_from_input_bad_kerning(path) -> tuple[int, int]:
    lines = load_input(path)
    raw_time, raw_distance = lines
    raw_time = raw_time[6:].replace(" ", "").replace("\n", "")
    raw_distance = raw_distance[10:].replace(" ", "").replace("\n", "")
    return int(raw_time), int(raw_distance)
