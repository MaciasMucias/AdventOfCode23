import itertools
from collections import namedtuple
from enum import Enum

Direction = namedtuple("Direction", ["dy", "dx"])
Point = namedtuple("Point", ["y", "x"])
Vector = namedtuple("Move", ["point", "direction"])


class Directions(Direction, Enum):
    LEFT: Direction = Direction(0, -1)
    UP: Direction = Direction(-1, 0)
    RIGHT: Direction = Direction(0, 1)
    DOWN: Direction = Direction(1, 0)


def load_input(path) -> list[str]:
    with open(path, "r") as f:
        lines = f.readlines()
    no_newline_lines = list(map(lambda x: x.replace("\n", ""), lines))
    return no_newline_lines


def paired(iterator):
    if len(iterator) % 2 != 0:
        raise RuntimeError("Not pairable")

    arr_range = iter(iterator)
    return iter(lambda: tuple(itertools.islice(arr_range, 2)), ())


def columnwise_list(list_of_lists: list[list] | tuple[tuple, ...]):
    return list(zip(*list_of_lists))


def list_of_strings_to_list_of_lists(list_of_strings: list[str]) -> list[list[str]]:
    return list(map(list, list_of_strings))


def move(location: Point, direction: Direction) -> Point:
    return Point(location[0] + direction[0], location[1] + direction[1])
