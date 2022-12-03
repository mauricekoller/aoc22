with open('Day2\input.txt', 'r') as input:
    games = input.read().rstrip()
    games = games.splitlines()

    total_points = 0
    shape_score = {'X': 1, 'Y': 2, 'Z': 3}
    analysis = {'win': ['A Y', 'B Z', 'C X'], 'draw': ['A X', 'B Y', 'C Z']}

    for game in games:
        secondletter = game[2:]
        if (game in analysis['win']):
            outcome_score = 6
        elif(game in analysis['draw']):
            outcome_score = 3
        else:
            outcome_score = 0
        score = shape_score[secondletter] + outcome_score
        total_points += score

    print(f'Result: {total_points}')
