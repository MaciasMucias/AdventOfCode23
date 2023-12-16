from abc import ABC, ABCMeta, abstractmethod

from src.utils import load_input, list_of_strings_to_list_of_lists, Direction



DIRECTIONS: dict[str, Direction] = {
    "LEFT": Direction(0, -1),
    "UP": Direction(-1, 0),
    "RIGHT": Direction(0, 1),
    "DOWN": Direction(1, 0)
}

HORIZONTAL: set[Direction] = {DIRECTIONS["LEFT"], DIRECTIONS["RIGHT"]}
VERTICAL: set[Direction] = {DIRECTIONS["UP"], DIRECTIONS["DOWN"]}

LEFT_REFLECTION: dict[Direction, Direction] = {
    DIRECTIONS["LEFT"]: DIRECTIONS["UP"],
    DIRECTIONS["DOWN"]: DIRECTIONS["RIGHT"],
    DIRECTIONS["RIGHT"]: DIRECTIONS["DOWN"],
    DIRECTIONS["UP"]: DIRECTIONS["LEFT"],
}

RIGHT_REFLECTION: dict[Direction, Direction] = {
    DIRECTIONS["LEFT"]: DIRECTIONS["DOWN"],
    DIRECTIONS["DOWN"]: DIRECTIONS["LEFT"],
    DIRECTIONS["RIGHT"]: DIRECTIONS["UP"],
    DIRECTIONS["UP"]: DIRECTIONS["RIGHT"],
}


def get_final_subclasses(cls: type) -> list:
    subclasses: list[type] = cls.__subclasses__()
    if not subclasses:
        return [cls]

    final_subclasses = []
    for subclass in subclasses:
        final_subclasses.extend(get_final_subclasses(subclass))

    return final_subclasses


class Element(ABC):
    @property
    @abstractmethod
    def char(self):
        pass

    def __new__(cls, char):
        subclass_map = {subclass.char: subclass for subclass in get_final_subclasses(cls)}
        subclass = subclass_map[char]
        instance = super(Element, subclass).__new__(subclass)
        return instance

    def __init__(self, _):
        self.energized = False
        self.visited_going_from: set[Direction] = set()

    def __str__(self):
        if self.energized:
            return "#"
        return self.char

    @abstractmethod
    def _propagate_light(self, direction: Direction) -> list[Direction]:
        pass

    def propagate_light(self, direction: Direction) -> list[Direction]:
        if direction in self.visited_going_from:
            return []
        self.visited_going_from.add(direction)
        self.energized = True
        return self._propagate_light(direction)


class Empty(Element):
    char = "."

    def _propagate_light(self, direction: Direction) -> list[Direction]:
        return [direction]


class Mirror(Element, ABC):
    @property
    @abstractmethod
    def reflection(self):
        pass

    def _propagate_light(self, direction: Direction) -> list[Direction]:
        return [self.reflection[direction]]


class LeftMirror(Mirror):
    char = "\\"
    reflection = LEFT_REFLECTION


class RightMirror(Mirror):
    char = "/"
    reflection = RIGHT_REFLECTION


class Splitter(Element, ABC):
    @property
    @abstractmethod
    def alignment(self):
        pass

    def _propagate_light(self, direction: Direction) -> list[Direction]:
        if direction in self.alignment:
            return [direction]
        return list(self.alignment)


class HorizontalSplitter(Splitter):
    char = "-"
    alignment = HORIZONTAL


class VerticalSplitter(Splitter):
    char = "|"
    alignment = VERTICAL


def parse_elements_from_input(path: str) -> list[list[Element]]:
    lines = load_input(path)
    element_map: list[list] = list_of_strings_to_list_of_lists(lines)

    for ind_y, row in enumerate(element_map):
        for ind_x, char in enumerate(row):
            element_map[ind_y][ind_x] = Element(char)

    return element_map


def count_all_energized_elements(element_map: list[list[Element]]) -> int:
    count = 0
    for row in element_map:
        for element in row:
            if element.energized:
                count += 1
    return count
