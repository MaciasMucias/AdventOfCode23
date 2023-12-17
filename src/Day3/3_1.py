from utils import get_parsed_input, get_surrounding_spaces


def get_all_surrounding_spaces(positions: list[tuple]) -> list[tuple]:
    spaces = []
    for position in positions:
        spaces.extend(get_surrounding_spaces(position))
    return spaces


parts_positions, parts, symbol_positions = get_parsed_input("../../Inputs/3")

found_parts = set()
for symbol_neighbours in get_all_surrounding_spaces(symbol_positions):
    x, y = symbol_neighbours
    found_parts.add(parts_positions.get(y, {}).get(x))


if None in found_parts:
    found_parts.remove(None)


parts_sum = 0
for part in found_parts:
    parts_sum += parts[part]

print(parts_sum)
