import re
from collections import deque
from src.utils import load_input


def parse_node_from_line(line: str) -> tuple[str, tuple[str, str]]:
    line_pattern = r"([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)"
    matches = re.match(line_pattern, line)
    return matches.group(1), (matches.group(2), matches.group(3))


def parse_maps_from_input(path) -> tuple[list[int], dict[str, tuple[str, str]]]:
    lines = load_input(path)
    steps = lines[0].replace("L", "0").replace("R", "1")
    int_steps = list(map(int, list(steps)))
    node_map = {}
    for line in lines[2:]:
        key, value = parse_node_from_line(line)
        node_map[key] = value
    return int_steps, node_map
