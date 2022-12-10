with open('Day4/input.txt', 'r') as input:
    crews = input.read().rstrip().splitlines()

    pairs = 0
    for crew in crews:
        first_member, second_member = [member.split('-') for member in crew.split(',')]
        first_range = set(range(int(first_member[0]), int(first_member[1])+1))
        second_range = set(range(int(second_member[0]), int(second_member[1])+1))

        if first_range <= second_range or first_range >= second_range:
            pairs += 1

    print(f'Result: {pairs}')
