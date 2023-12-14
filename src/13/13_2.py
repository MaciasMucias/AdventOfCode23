from src.utils import columnwise_list
from utils import parse_input, find_reflection, find_reflection_with_smudge

patterns = parse_input("../../Inputs/13")

total_value = 0

for i, pattern in enumerate(patterns):
    horizontal_reflection = None
    vertical_reflection = None
    if (value := find_reflection(pattern)) is not None:
        vertical_reflection = value
    elif (value := find_reflection(columnwise_list(pattern))) is not None:
        horizontal_reflection = value

    if (value := find_reflection_with_smudge(pattern, old_reflection=vertical_reflection)) is not None:
        total_value += 100*value
    elif (value := find_reflection_with_smudge(columnwise_list(pattern), old_reflection=horizontal_reflection)) is not None:
        total_value += value
print(total_value)
