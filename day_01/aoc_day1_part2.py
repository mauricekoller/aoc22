with open('Day1\input.txt', 'r') as input:
    calories = input.read().rstrip()
    calories = calories.splitlines()
    elves = [0]
    counter = 0
    for element in calories:
        if (element == ''):
            counter += 1
            elves.append(0)
        else:
            elves[counter] += int(element)
    elves.sort(reverse=True)
    carried_calories = 0
    for i in range(3):
        carried_calories += elves[i]
    print(f'Max Value: {max(elves)}')
    print(f'Top3 Calories: {carried_calories}')
