from utils import get_parsed_input, get_surrounding_spaces


def calculate_gear_ratio(coordinate: tuple, existing_parts_positions: dict[dict[int]], existing_parts: dict[int]) -> int:
    _, _, char = coordinate
    if char != "*":
        return 0

    surrounding_parts = set()

    for possible_part in get_surrounding_spaces(coordinate):
        x, y = possible_part
        surrounding_parts.add(existing_parts_positions.get(y, {}).get(x))

    if None in surrounding_parts:
        surrounding_parts.remove(None)

    if len(surrounding_parts) != 2:
        return 0

    return existing_parts[surrounding_parts.pop()] * existing_parts[surrounding_parts.pop()]


parts_positions, parts, symbol_positions = get_parsed_input("../../Inputs/3")


parts_sum = 0
for symbol in symbol_positions:
    parts_sum += calculate_gear_ratio(symbol, parts_positions, parts)

print(parts_sum)
