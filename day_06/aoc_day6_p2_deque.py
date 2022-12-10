from collections import deque

with open('day_06/input.txt', 'r') as input:
    text = input.read().rstrip()
    marker_len = 14

    sliding_window = deque(text[0:marker_len])
    print(sliding_window)

    for i in range(marker_len, len(text)):
        duplicates = {x for x in sliding_window if sliding_window.count(x) > 1}
        if not duplicates:
            print(f'First Index with no Duplicate: {i}')
            break
        sliding_window.popleft()
        sliding_window.append(text[i])
