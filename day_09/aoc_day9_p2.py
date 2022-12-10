with open('day_09/input.txt', 'r') as input:
    rope_len = 10
    text_lines = input.read().rstrip().splitlines()
    position_rope_element = [[0, 0] for _ in range(rope_len+1)]

    # Add starting position by default
    tail_positions = set([(0, 0)])

    # "Array" starts at [0,0] increasing to the right/upwards
    for line in text_lines:
        move_dir, move_len = line.split(' ')

        # Move Head one position at a time
        # Then for each nth element of the rope check distance to n-1 element and move it accordingly if necessary
        # If last element (tail) has been moved add Tail Position as a Tuple to Set --> No duplicates
        for _ in range(int(move_len)):

            # Move Head
            match move_dir:
                case 'L':
                    position_rope_element[0][0] -= 1
                case 'R':
                    position_rope_element[0][0] += 1
                case 'U':
                    position_rope_element[0][1] += 1
                case 'D':
                    position_rope_element[0][1] -= 1

            # Check if Tail and Head are seperated
            # If Distance is bigger than one: Move Tail one position towards Head, If Distance is Diagonal, move Diagonally towards Head
            # .....    .....    .....
            # .....    ..H..    ..H..
            # ..H.. -> ..... -> ..T..
            # .T...    .T...    .....
            # .....    .....    .....
            for member in range(1, rope_len):
                distance = [h-t for h, t in zip(position_rope_element[member-1], position_rope_element[member])]
                # Create movement instruction: If Distance is 2 subtract/add one, else keep it the same
                # Examples: [2,1] -move-> [1,1]     [-2,0] -move-> [-1,0]       [2,0] -move-> [1,0]
                if any(abs(value) >= 2 for value in distance):
                    tail_movement = [val-1 if val == 2 else val+1 if val == -2 else val for val in distance]
                    position_rope_element[member] = [t+m for t, m in zip(position_rope_element[member], tail_movement)]
                    if (member == rope_len-1):
                        tail_positions.add(tuple(position_rope_element[member]))

    print(f'Number of Positions the Tail visited: {len(tail_positions)}')
