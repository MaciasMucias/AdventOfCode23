from src.utils import columnwise_list
from utils import parse_input, find_reflection

patterns = parse_input("../../Inputs/13")

total_value = 0
for pattern in patterns:
    if (value := find_reflection(pattern)) is not None:
        total_value += 100*value
    elif (value := find_reflection(columnwise_list(pattern))) is not None:
        total_value += value
print(total_value)
