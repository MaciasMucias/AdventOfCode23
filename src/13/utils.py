from src.utils import load_input


def find_reflection(pattern: list[list[str]]) -> int | None:
    for i in range(len(pattern) - 1):
        to_start = i + 1
        to_end = len(pattern) - to_start
        for j in range(min(to_start, to_end)):
            if pattern[i-j] != pattern[i+1+j]:
                break
        else:
            return to_start
    return None


def is_reflection_with_smudge(line1: list[str], line2: list[str]) -> bool:
    smudge_found = False
    for a, b in zip(line1, line2):
        if a != b:
            if smudge_found:
                return False
            smudge_found = True
    return True


def parse_input(path: str) -> list[list[list[str]]]:
    lines = load_input(path)
    split_lines = list(map(list, lines))
    patterns = []
    pattern = []
    for line in split_lines:
        if not line:
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append(line)
    patterns.append(pattern)
    return patterns
