with open('input.txt', 'r') as input:
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
    print(f'Max Value: {max(elves)}')
