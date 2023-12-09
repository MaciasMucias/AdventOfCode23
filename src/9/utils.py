import itertools
from typing import Literal

from src.utils import load_input


def parse_reports_from_input(path) -> list[list[int]]:
    lines = load_input(path)
    return [list(map(int, line.split())) for line in lines]


def get_differences(values: list[int]) -> list[int]:
    return [b - a for a, b in itertools.pairwise(values)]


def helper_subtract(x, y):
    return x-y

def helper_sum(x, y):
    return x+y

def predict_extra_value(values: list[int], *, extra: Literal["prev", "next"]) -> int:
    if extra not in ["prev", "next"]:
        raise ValueError(f"Incorrect value for argument forwards: {extra}")

    index = 0 if extra == "prev" else -1
    val_operation = helper_subtract if extra == "prev" else helper_sum

    if not any(values):  # all zeros
        return 0

    differences = get_differences(values)
    differences_extra_value = predict_extra_value(differences, extra=extra)
    return val_operation(values[index], differences_extra_value)
