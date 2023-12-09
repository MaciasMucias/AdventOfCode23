import itertools

from src.utils import load_input


def parse_reports_from_input(path) -> list[list[int]]:
    lines = load_input(path)
    return [list(map(int, line.split())) for line in lines]


def get_differences(values: list[int]) -> list[int]:
    return [b-a for a, b in itertools.pairwise(values)]


def predict_next_value(values: list[int]) -> int:
    if not any(values):  # all zeros
        return 0

    differences = get_differences(values)
    differences_next_value = predict_next_value(differences)
    return values[-1] + differences_next_value
