import itertools
import operator

from src.utils import load_input


def parse_map_from_line(line: str) -> tuple[int, int, int]:
    raw_values = line.split(" ")
    int_values = map(int, raw_values)
    destination_start, source_start, conversion_range = int_values
    source_end = source_start + conversion_range - 1
    conversion_bias = destination_start - source_start
    return source_start, source_end, conversion_bias


def parse_conversion_type(line: str) -> tuple[str,  str]:
    trimmed_line = line[:-5]
    source, _, destination = trimmed_line.split("-")
    return source, destination


def parse_seeds(line: str) -> list[int]:
    trimmed_line = line[7:]
    seeds = list(map(int, trimmed_line.split(" ")))
    return seeds


def parse_map(lines: list[str]) -> tuple[str, tuple[str, list[tuple[int, int, int]]]]:
    map_source, map_destination = parse_conversion_type(lines[0])
    map_conversions = [parse_map_from_line(line) for line in lines[1:]]
    map_conversions.sort(key=operator.itemgetter(0))
    return map_source, (map_destination, map_conversions)


def parse_input(path) -> tuple[list, dict[str, tuple[str, list[tuple[int, int, int]]]]]:
    lines = load_input(path)
    seeds = parse_seeds(lines[0])
    maps = {}
    empty_lines = [i for i, x in enumerate(lines) if x == ""]
    empty_lines.append(None)
    for start, end in itertools.pairwise(empty_lines):
        key, value = parse_map(lines[start+1: end])
        maps[key] = value

    return seeds, maps


def get_destination_from_map(source_value, map_data: list[tuple[int, int, int]]):
    low, high = 0, len(map_data) - 1

    while low <= high:
        middle = (low+high) // 2

        if map_data[middle][0] <= source_value <= map_data[middle][1]:
            return source_value + map_data[middle][2]

        if map_data[middle][0] > source_value:
            high = middle - 1
        else:
            low = middle + 1
    return source_value
