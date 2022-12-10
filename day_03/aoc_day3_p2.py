with open('day_03\input.txt', 'r') as input:
    items = input.read().rstrip()
    items = items.splitlines()

    total_points = 0
    # Use Zip List Compression to always return tripplets
    for elf_1, elf_2, elf_3 in zip(items[0::3], items[1::3], items[2::3]):
        for letter in elf_1:
            if letter in elf_2 and letter in elf_3:
                similarity = letter
                # Convert Char to Unicode Number: lowercase starts at 97 Uppercase starts at 65 so we need to offset to start at 1 and 27 respectively
                if similarity.islower():
                    priority = ord(similarity)-96
                else:
                    priority = ord(similarity)-38
                break
        total_points += priority

    print(f'Result: {total_points}')
