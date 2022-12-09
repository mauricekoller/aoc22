with open('Day9/input.txt', 'r') as input:
    text_lines = input.read().rstrip().splitlines()
    position_head = [0,0]
    position_tail = [0,0]

    tail_positions = []

    # "Array" starts at [0,0] increasing to the right/upwards
    for line in text_lines:
        move_dir, move_len = line.split(' ')

        # Move Head one position at a time
        # Afterwards check if Distance to Tail exists and move it accordingly if necessary
        # After move add new position of Tail to List? --> At the End make a set from the list to remove duplicates! and count
        for _ in range(move_len):
            # Move Head
            match move_dir:
                case 'L':
                    position_head[0]-=1
                case 'R':
                    position_head[0]+=1
                case 'U':
                    position_head[1]+=1
                case 'D':
                    position_head[1]-=1
                
            # Check if tail needs to be moved
            


    print(f'Number of all visible Trees: {0}')
