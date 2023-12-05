from itertools import islice
from src.utils import load_input

COLORS = ["R", "G", "B"]


def paired(iterator):
    if len(iterator) % 2 != 0:
        raise RuntimeError("Not pairable")

    arr_range = iter(iterator)
    return iter(lambda: tuple(islice(arr_range, 2)), ())


def get_parsed_input(path):
    lines = load_input(path)
    games = [line_to_game(line) for line in lines]
    return games


def line_to_game(line: str):
    line = line
    semicolon_index = line.find(":")
    game_id = int(line[5:semicolon_index])
    subsets_long_string = line[semicolon_index + 1:]
    subsets_long_string = subsets_long_string.replace(",", "")
    subsets_strings = subsets_long_string.split(";")

    subsets = []
    for subset_string in subsets_strings:
        subset_string = subset_string.removeprefix(" ")
        tokens = subset_string.split(" ")
        value: str
        key: str
        subset = {color: 0 for color in COLORS}
        for value, key in paired(tokens):
            subset[key.upper()[0]] = int(value)
        subsets.append(subset)
    return game_id, subsets
