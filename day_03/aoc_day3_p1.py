with open('day_03\input.txt', 'r') as input:
    items = input.read().rstrip()
    items = items.splitlines()

    total_points = 0
    for item in items:
        item_len_half = int(len(item)/2)
        first_half = item[:item_len_half]
        second_half = item[item_len_half:]
        for letter in first_half:
            if letter in second_half:
                similarity = letter
                # Convert Char to Unicode Number: lowercase starts at 97 Uppercase starts at 65 so we need to offset to start at 1 and 27 respectively
                if similarity.islower():
                    priority = ord(similarity)-96
                else:
                    priority = ord(similarity)-38
                break
        total_points += priority

    print(f'Result: {total_points}')
