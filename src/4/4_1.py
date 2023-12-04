from utils import parse_games_from_input


games = parse_games_from_input("../../Inputs/4")


total_points = 0
for game in games:
    game_id, winning_numbers, player_numbers = game
    player_winning_numbers = winning_numbers & player_numbers
    if len(player_winning_numbers) == 0:
        continue
    point_exponent = len(player_winning_numbers) - 1
    total_points += 2**point_exponent

print(total_points)
