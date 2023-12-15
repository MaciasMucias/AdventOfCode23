from utils import parse_init_seq_from_input, custom_hash


strings = parse_init_seq_from_input("../../Inputs/15")

hash_sum = 0
for string in strings:
    hash_sum += custom_hash(string)

print(hash_sum)
