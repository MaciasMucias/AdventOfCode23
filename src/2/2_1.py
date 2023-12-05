from utils import get_parsed_input

MAXIMUM = {"R": 12, "G": 13, "B": 14}

valid_games = []
for game_id, subsets in get_parsed_input("../../Inputs/2"):
    for subset in subsets:
        if subset["R"] > MAXIMUM["R"] or \
                subset["G"] > MAXIMUM["G"] or \
                subset["B"] > MAXIMUM["B"]:
            break
    else:
        valid_games.append(game_id)

print(sum(valid_games))
