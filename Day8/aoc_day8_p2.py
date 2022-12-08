with open('Day8/input.txt', 'r') as input:
    text_lines = input.read().rstrip().splitlines()

    forest = []
    best_scenery = 0

    for line in text_lines:
        forest.append([int(x) for x in line])

    # Add Perimeter as visible
    x_dim = len(forest[0])
    y_dim = len(forest)

    # Check all internal Fields
    for x in range(1, x_dim-1):
        for y in range(1, y_dim-1):
            range_a = 1
            range_l = 1
            range_r = 1
            range_b = 1
            current_tree = forest[x][y]
            # Check all trees above
            for x_i in range(x-1, 0, -1):
                if (forest[x_i][y] < current_tree):
                    range_a += 1
                else:
                    break
            # Chek all trees below
            for x_i in range(x+1, x_dim-1):
                if (forest[x_i][y] < current_tree):
                    range_b += 1
                else:
                    break
            # Check all trees left
            for y_i in range(y-1, 0, -1):
                if (forest[x][y_i] < current_tree):
                    range_l += 1
                else:
                    break
            # Check all trees right
            for y_i in range(y+1, y_dim-1):
                if (forest[x][y_i] < current_tree):
                    range_r += 1
                else:
                    break
            new_scenery = range_a*range_b*range_l*range_r
            print(f'scenery x:{x} y:{y} has score: {new_scenery} because {range_a} {range_b} {range_l} {range_r}')
            if best_scenery < new_scenery:
                best_scenery = new_scenery

    print(f'Scenery Score: {best_scenery}')
