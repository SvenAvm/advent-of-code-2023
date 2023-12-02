import utils


starting_games_high = utils.parse_high_game_scores_from_file("input.txt")
starting_games_low = utils.parse_low_game_scores_from_file("input.txt")

filtered_games = utils.filter_games_by_possible_high_scores(starting_games_high, utils.possible_cubes)


print(f"""
Solution to task 1: {utils.get_solution_1(filtered_games)}
Solution to task 2: {utils.get_solution_2(starting_games_high)}
""")


