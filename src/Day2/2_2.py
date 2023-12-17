from utils import get_parsed_input


game_power = []
for game_id, subsets in get_parsed_input("../../Inputs/2"):
    subsets_iter = iter(subsets)
    first_subset = next(subsets_iter)
    minimum = first_subset
    for subset in subsets_iter:
        minimum["R"] = max(minimum["R"], subset["R"])
        minimum["G"] = max(minimum["G"], subset["G"])
        minimum["B"] = max(minimum["B"], subset["B"])
    game_power.append(minimum["R"] * minimum["G"] * minimum["B"])

print(sum(game_power))
