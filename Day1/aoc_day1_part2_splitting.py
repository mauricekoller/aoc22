with open('input.txt', 'r') as input:
    input_str = input.read()
    chunks_of_elves = input_str.split('\n\n')
    print(chunks_of_elves)
    single_lines = []
    for chunk in chunks_of_elves:
        single_lines.append(chunk.split('\n'))
    print(single_lines)
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
