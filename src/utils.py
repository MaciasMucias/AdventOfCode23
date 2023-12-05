def load_input(path):
    with open(path, "r") as f:
        lines = f.readlines()
    no_newline_lines = list(map(lambda x: x.replace("\n", ""), lines))
    return no_newline_lines
