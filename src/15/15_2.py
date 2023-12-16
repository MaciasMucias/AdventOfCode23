from collections import OrderedDict
from utils import parse_init_seq_from_input, custom_hash


strings = parse_init_seq_from_input("../../Inputs/15")

boxes = [OrderedDict() for i in range(256)]

for string in strings:
    if string[-1] == "-":
        label = string[:-1]
        target_box = custom_hash(label)
        if label in boxes[target_box]:
            boxes[target_box].pop(label)

    else:
        label = string[:-2]
        lens_power = int(string[-1])
        target_box = custom_hash(label)
        boxes[target_box][label] = lens_power

total_focusing_power = 0
for ind, box in enumerate(boxes, 1):
    for pos, lens in enumerate(box.values(), 1):
        total_focusing_power += ind * pos * lens

print(total_focusing_power)
