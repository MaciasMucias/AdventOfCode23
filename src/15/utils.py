from src.utils import load_input


def parse_init_seq_from_input(path) -> list[str]:
    return load_input(path)[0].split(",")


def custom_hash(string: str) -> int:
    value = 0
    for c in string:
        value += ord(c)
        value *= 17
        value %= 256
    return value

