from src.utils import load_input


def extract_numbers_from_line(line: str, number_id):
    padded_line = line + "."

    number_positions = {}
    numbers = {}

    number = ""
    number_spots = []
    reading_number = False
    for ind, char in enumerate(padded_line):
        if char.isnumeric():
            reading_number = True
            number += char
            number_spots.append(ind)
        elif reading_number:
            for spot in number_spots:
                number_positions[spot] = number_id
            numbers[number_id] = int(number)
            number_id += 1

            number = ""
            number_spots = []
            reading_number = False

    return number_positions, numbers, number_id


def abstract_map(map_strings: list[str]) -> tuple[dict, dict, list]:
    number_positions = {}
    numbers = {}
    symbol_positions = []

    number_id = 0

    for row, line in enumerate(map_strings):
        line = line.replace("\n", "")
        new_positions, new_numbers, updated_number_id = extract_numbers_from_line(line, number_id)
        number_positions[row] = new_positions
        numbers.update(new_numbers)
        number_id = updated_number_id

        for column, char in enumerate(line):
            if not char.isdigit() and char != ".":
                symbol_positions.append((row, column))

    return number_positions, numbers, symbol_positions


def get_surrounding_spaces(coordinates: list) -> list[tuple]:
    spaces = []
    for x, y in coordinates:
        spaces.extend([
            (y-1, x-1),
            (y-1, x),
            (y-1, x+1),
            (y, x-1),
            (y, x+1),
            (y+1, x-1),
            (y+1, x),
            (y+1, x+1),
        ])
    return spaces


def get_parsed_input(path) -> tuple[dict[dict], dict[int], list]:
    lines = load_input(path)
    return abstract_map(lines)
