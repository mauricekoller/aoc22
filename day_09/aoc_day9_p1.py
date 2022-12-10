with open('day_09/input.txt', 'r') as input:
    text_lines = input.read().rstrip().splitlines()
    position_head = [0, 0]
    position_tail = [0, 0]

    # Add starting position by default
    tail_positions = set([(0, 0)])

    # "Array" starts at [0,0] increasing to the right/upwards
    for line in text_lines:
        move_dir, move_len = line.split(' ')

        # Move Head one position at a time
        # Afterwards check if Distance to Tail exists and move it accordingly if necessary
        # After move add new position of Tail as a Tuple to Set --> No duplicates
        for _ in range(int(move_len)):

            # Move Head
            match move_dir:
                case 'L':
                    position_head[0] -= 1
                case 'R':
                    position_head[0] += 1
                case 'U':
                    position_head[1] += 1
                case 'D':
                    position_head[1] -= 1

            # Check if Tail and Head are seperated
            # If Distance is bigger than one: Move Tail one position towards Head, If Distance is Diagonal, move Diagonally towards Head
            # .....    .....    .....
            # .....    ..H..    ..H..
            # ..H.. -> ..... -> ..T..
            # .T...    .T...    .....
            # .....    .....    .....
            distance = [h-t for h, t in zip(position_head, position_tail)]
            # Create movement instruction: If Distance is 2 subtract/add one, else keep it the same
            # Examples: [2,1] -move-> [1,1]     [-2,0] -move-> [-1,0]       [2,0] -move-> [1,0]
            if any(abs(value) >= 2 for value in distance):
                tail_movement = [val-1 if val == 2 else val+1 if val == -2 else val for val in distance]
                position_tail = [t+m for t, m in zip(position_tail, tail_movement)]
                tail_positions.add(tuple(position_tail))

    print(f'Number of Positions the Tail visited: {len(tail_positions)}')
