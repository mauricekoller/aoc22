with open('Day8/input.txt', 'r') as input:
    text_lines = input.read().rstrip().splitlines()

    forest = []
    visible_trees = 0

    for line in text_lines:
        forest.append([int(x) for x in line])

    # Add Perimeter as visible
    x_dim = len(forest[0])
    y_dim = len(forest)
    visible_trees += (2*x_dim-2 + 2*y_dim-2)
    print(visible_trees)

    for row in forest:
        print(row)

    # Check all internal Fields
    for x in range(1, x_dim-1):
        for y in range(1, y_dim-1):
            visible_a = True
            visible_b = True
            visible_l = True
            visible_r = True
            current_tree = forest[x][y]
            print(f'Checking for Tree {x} {y} height: {current_tree}')
            # Check all trees above
            for x_i in range(0, x):
                if (forest[x_i][y] >= current_tree):
                    visible_a = False
                    break
            # Chek all trees below
            for x_i in range(x+1, x_dim):
                if (forest[x_i][y] >= current_tree):
                    visible_b = False
                    break
            # Check all trees left
            for y_i in range(0, y):
                if (forest[x][y_i] >= current_tree):
                    visible_l = False
                    break
            # Check all trees right
            for y_i in range(y+1, y_dim):
                if (forest[x][y_i] >= current_tree):
                    visible_r = False
                    break
            if visible_a or visible_b or visible_l or visible_r:
                visible_trees += 1

    print(f'Number of all visible Trees: {visible_trees}')
