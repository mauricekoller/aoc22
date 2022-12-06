with open('Day6/input.txt', 'r') as input:
    text = input.read().rstrip()
    marker_len = 14

    for i in range(marker_len, len(text)):
        slice = text[i-marker_len:i]
        duplicates = {x for x in slice if slice.count(x) > 1}
        if not duplicates:
            print(f'First Index with no Duplicate: {i}')
            break
