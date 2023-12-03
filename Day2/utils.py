possible_cubes = {"blue": 14, "green": 13, "red": 12}


def parse_high_game_scores(text):
    parsed_data = []

    # split input into individual games and skip the first empty split
    games = text.split('Game')[1:]

    for game in games:
        game_number, game_content = game.split(':', 1)
        game_scores = {'game_number': int(game_number.strip()), 'blue': 0, 'green': 0, 'red': 0}

        # split game into individual score entries
        score_entries = game_content.split(';')
        for entry in score_entries:
            scores = entry.split(',')

            # update game_scores with the highest score of each player in this game
            for score in scores:
                points, player = score.strip().split()
                if int(points) > game_scores[player]:
                    game_scores[player] = int(points)
        parsed_data.append(game_scores)

    return parsed_data


def parse_low_game_scores(text):
    parsed_data = []

    # split input into individual games and skip the first empty split
    games = text.split('Game')[1:]

    for game in games:
        game_number, game_content = game.split(':', 1)
        game_scores = {'game_number': int(game_number.strip()), 'blue': float('inf'), 'green': float('inf'), 'red': float('inf')}

        # split game into individual score entries
        score_entries = game_content.split(';')
        for entry in score_entries:
            scores = entry.split(',')

            # update game_scores with the lowest score of each player in this game
            for score in scores:
                points, player = score.strip().split()
                if int(points) < game_scores[player]:
                    game_scores[player] = int(points)
        parsed_data.append(game_scores)

    return parsed_data


def parse_high_game_scores_from_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return parse_high_game_scores(text)


def parse_low_game_scores_from_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return parse_low_game_scores(text)


def filter_games_by_possible_high_scores(parsed_scores, possible):
    filtered_games = []

    for game in parsed_scores:
        # check if all players scores are within possible_cubes
        if all(game[player] <= possible[player] for player in ["blue", "green", "red"]):
            filtered_games.append(game['game_number'])

    return filtered_games


def get_solution_1(filtered_games):
    return sum(filtered_games)


def get_solution_2(games):
    solution = 0
    for game in games:
        power = game['blue'] * game['red'] * game['green']
        solution += power

    return solution
