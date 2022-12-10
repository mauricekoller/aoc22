with open('day_06/input.txt', 'r') as input:
    text = input.read().rstrip()

    for i in range(4, len(text)):
        slice = text[i-4:i]
        duplicates = {x for x in slice if slice.count(x) > 1}
        if not duplicates:
            print(f'First Index with no Duplicate: {i}')
            break
