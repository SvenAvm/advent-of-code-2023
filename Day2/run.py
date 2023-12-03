import utils


high = utils.parse_high_game_scores_from_file("input.txt")

print(f"""
Solution to task 1: {utils.get_solution_1(utils.filter_games_by_possible_high_scores(high, utils.possible_cubes))}
Solution to task 2: {utils.get_solution_2(high)}
""")


