with open('Day2\input.txt', 'r') as input:
    games = input.read().rstrip()
    games = games.splitlines()

    total_points = 0
    shape_score = {'A': 1, 'B': 2, 'C': 3}
    outcome_score = {'X': 0, 'Y': 3, 'Z': 6}
    analysis = {'Z': ['A B', 'B C', 'C A'], 'Y': ['A A', 'B B', 'C C'], 'X': ['A C', 'B A', 'C B']}

    for game in games:
        firstletter = game[:1]
        secondletter = game[2:]

        strategy = analysis[secondletter]
        reaction = (element for element in strategy if element.startswith(firstletter))
        reaction_letter = reaction[2:]

        winning_score = outcome_score[secondletter]
        score = shape_score[reaction_letter] + winning_score
        total_points += score

    print(f'Result: {total_points}')
