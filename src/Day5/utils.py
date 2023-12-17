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


def parse_conversion_type(line: str) -> tuple[str, str]:
    trimmed_line = line[:-5]
    source, _, destination = trimmed_line.split("-")
    return source, destination


def parse_seeds(line: str) -> list[int]:
    trimmed_line = line[7:]
    seeds = list(map(int, trimmed_line.split(" ")))
    return seeds


def fill_map(conversions: list[tuple[int, int, int]]):
    filled_conversions = []
    working_copy = sorted(conversions, key=operator.itemgetter(0))
    for last_conversion, next_conversion in itertools.pairwise(working_copy):

        first_new_position = last_conversion[1] + 1
        filled_range = next_conversion[0] - first_new_position - 1
        if filled_range == -1:
            continue

        filled_conversions.append((first_new_position, first_new_position + filled_range, 0))

    filled_conversions.extend(conversions)
    return sorted(filled_conversions, key=operator.itemgetter(0))


def parse_map(lines: list[str]) -> tuple[str, tuple[str, list[tuple[int, int, int]]]]:
    map_source, map_destination = parse_conversion_type(lines[0])
    map_conversions = [parse_map_from_line(line) for line in lines[1:]]
    filled_map_conversions = fill_map(map_conversions)
    return map_source, (map_destination, filled_map_conversions)


def parse_input(path) -> tuple[list, dict[str, tuple[str, list[tuple[int, int, int]]]]]:
    lines = load_input(path)
    seeds = parse_seeds(lines[0])
    maps = {}
    empty_lines = [i for i, x in enumerate(lines) if x == ""]
    empty_lines.append(None)
    for start, end in itertools.pairwise(empty_lines):
        key, value = parse_map(lines[start + 1: end])
        maps[key] = value

    return seeds, maps


def find_responsible_mapping(source_value, map_data):
    low, high = 0, len(map_data) - 1

    while low <= high:
        middle = (low + high) // 2

        if map_data[middle][0] <= source_value <= map_data[middle][1]:
            return middle

        if map_data[middle][0] > source_value:
            high = middle - 1
        else:
            low = middle + 1
    return None


def get_all_responsible_mappings(source_slice: tuple[int, int], map_data: list[tuple[int, int, int]]):
    low_end = find_responsible_mapping(source_slice[0], map_data)
    high_end = find_responsible_mapping(source_slice[1], map_data)
    if high_end is None:
        if low_end is None:
            if source_slice[0] < map_data[0][0] and source_slice[1] > map_data[-1][1]:
                return map_data
            return []
        return map_data[low_end:]
    return map_data[low_end:high_end + 1]  # +Day1 is inclusive boundary


def combine_slices(slices: list[tuple[int, int]]):
    combined_slices = sorted(slices)

    i = 0
    while i < len(combined_slices) - 1:
        if combined_slices[i][1] >= combined_slices[i+1][0] - 1:
            second = combined_slices.pop(i + 1)
            first = combined_slices.pop(i)
            combined_slices.insert(i, (min(first[0], second[0]), max(first[1], second[1])))
        else:
            i += 1
    return combined_slices


def convert_whole_mapping_to_destination(mapping: tuple[int, int, int]) -> tuple[int, int]:
    return mapping[0] + mapping[2], mapping[1] + mapping[2]


def get_destination_slices_from_map(slices: list[tuple[int, int]], map_data: list[tuple[int, int, int]]):
    destination_slices = []

    for source_slice in slices:
        responsible_mappings = get_all_responsible_mappings(source_slice, map_data)
        if not responsible_mappings:
            destination_slices.append(source_slice)
            continue

        if len(responsible_mappings) == 1 and responsible_mappings[0][0] <= source_slice[0] and source_slice[1] <= responsible_mappings[0][1]:
            new_slice = (source_slice[0], source_slice[1], responsible_mappings[0][2])
            converted_slice = convert_whole_mapping_to_destination(new_slice)
            destination_slices.append(converted_slice)
            continue

        first_mapping = responsible_mappings[0]
        last_mapping = responsible_mappings[-1]
        if source_slice[0] >= first_mapping[0]:
            new_slice = (source_slice[0], first_mapping[1], first_mapping[2])
            converted_slice = convert_whole_mapping_to_destination(new_slice)
            destination_slices.append(converted_slice)
            start_offset = 1
        else:
            destination_slices.append((source_slice[0], first_mapping[0]-1))
            start_offset = None

        if source_slice[1] <= last_mapping[1]:
            new_slice = (last_mapping[0], source_slice[1], last_mapping[2])
            converted_slice = convert_whole_mapping_to_destination(new_slice)
            destination_slices.append(converted_slice)
            end_offset = -1
        else:
            destination_slices.append((last_mapping[1]+1, source_slice[1]))
            end_offset = None

        for mapping in responsible_mappings[start_offset:end_offset]:
            converted_slice = convert_whole_mapping_to_destination(mapping)
            destination_slices.append(converted_slice)

    return combine_slices(destination_slices)


def get_destination_from_map(source_value: int, map_data: list[tuple[int, int, int]]):
    mapping_index = find_responsible_mapping(source_value, map_data)
    if mapping_index is None:
        return source_value
    return source_value + map_data[mapping_index][2]
