import itertools


def load_input(path):
    with open(path, "r") as f:
        lines = f.readlines()
    no_newline_lines = list(map(lambda x: x.replace("\n", ""), lines))
    return no_newline_lines


def paired(iterator):
    if len(iterator) % 2 != 0:
        raise RuntimeError("Not pairable")

    arr_range = iter(iterator)
    return iter(lambda: tuple(itertools.islice(arr_range, 2)), ())