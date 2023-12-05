from src.utils import load_input


def parse_game_from_line(line: str) -> tuple[int, set, set]:
    line = line
    semicolon_index = line.find(":")
    game_id = int(line[5:semicolon_index])
    game_data = line[semicolon_index + 1:]
    winning_numbers, player_numbers = game_data.split("|")
    winning_numbers = winning_numbers.replace("  ", " ").removeprefix(" ").removesuffix(" ")
    player_numbers = player_numbers.replace("  ", " ").removeprefix(" ").removesuffix(" ")
    set_of_winning_numbers = set(winning_numbers.split(" "))
    set_of_player_numbers = set(player_numbers.split(" "))
    return game_id, set_of_winning_numbers, set_of_player_numbers


def parse_games_from_input(path) -> list[tuple[int, set, set]]:
    lines = load_input(path)
    games = [parse_game_from_line(line) for line in lines]
    return games
