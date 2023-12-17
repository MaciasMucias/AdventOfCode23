from utils import parse_games_from_input


def award_extra_scratchcards(winning_card, amount_won, scratchcards):
    for i in range(amount_won):  # winning cards start index at Day1, so -Day1 has to be subtracted, this is contained
        # inside the range which is [0, amount_won) instead of [Day1, amount_won]
        scratchcards[winning_card + i] += scratchcards[winning_card - 1]


games = parse_games_from_input("../../Inputs/4")

scratchcards_count = [1] * len(games)

for game in games:
    game_id, winning_numbers, player_numbers = game
    player_winning_numbers = winning_numbers & player_numbers
    if len(player_winning_numbers) == 0:
        continue
    award_extra_scratchcards(game_id, len(player_winning_numbers), scratchcards_count)

print(sum(scratchcards_count))
