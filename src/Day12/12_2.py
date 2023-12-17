from utils import parse_springs_from_input, number_of_solutions


data = parse_springs_from_input("../../Inputs/12")

all_solutions = 0
for springs, numbers in data:
    all_solutions += number_of_solutions("?".join([springs]*5)+".", numbers*5)

print(all_solutions)
