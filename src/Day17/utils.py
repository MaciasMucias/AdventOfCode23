from math import inf
from collections import defaultdict
from heapq import heappush, heappop

from src.utils import load_input, Point, Direction


def parse_heat_loss_map_from_input(path) -> list[list[int]]:
    lines = load_input(path)
    heat_loss_map = [list(map(int, list(line))) for line in lines]
    return heat_loss_map


def find_least_heat_loss_path(heat_map: list[list[int]], lower_bound, higher_bound) -> int:
    w, h = len(heat_map[0]), len(heat_map)
    start = Point(0, 0)
    end = Point(h-1, w-1)
    distances = defaultdict(lambda: inf)
    queue = [(0, (start, Direction(0, 1))), (0, (start, Direction(1, 0)))]

    while queue:
        cost, (point, direction) = heappop(queue)
        if point == end:
            return cost
        if cost > distances[point, direction]:
            continue
        y, x = point.y, point.x
        dy, dx = direction.dy, direction.dx
        for new_dy, new_dx in ((-dx, dy), (dx, -dy)):
            new_cost = cost
            for dist in range(1, higher_bound + 1):
                new_y, new_x = y + new_dy * dist, x + new_dx * dist
                if 0 <= new_y < h and 0 <= new_x < w:
                    new_cost += heat_map[new_y][new_x]
                    if dist < lower_bound:
                        continue
                    key = (Point(new_y, new_x), Direction(new_dy, new_dx))
                    if new_cost < distances[key]:
                        distances[key] = new_cost
                        heappush(queue, (new_cost, key))
    return -1
