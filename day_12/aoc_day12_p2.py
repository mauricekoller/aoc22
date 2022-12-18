from colorama import Fore, Back, Style
from time import sleep
import os


def find_all_pos(nodes, letter):
    pos = []
    for y, line in enumerate(nodes):
        for x, val in enumerate(line):
            if nodes[y][x] == letter:
                pos.append([y, x])
    return pos


def find_pos(nodes, letter):
    for i, line in enumerate(nodes):
        pos = -1
        try:
            pos = line.index(letter)
        except ValueError:
            pass
        if pos >= 0:
            return ([i, pos])


def check_inside(node, x_dim, y_dim):
    if all([True if coord >= 0 else False for coord in node]) and node[0] <= y_dim and node[1] <= x_dim:
        return True
    else:
        return False


def letter_reachable(current_letter, next_letter):
    # edge Cases for S and E
    if current_letter == 'S' and next_letter == 'a':
        return True
    if next_letter == 'E' and current_letter == 'z':
        return True
    # base case
    if ord(next_letter)-ord(current_letter) <= 1 and current_letter != 'S' and next_letter != 'E':
        return True
    else:
        return False


def print_maze(nodes, visited, to_visit):
    os.system('clear')
    for y, row in enumerate(nodes):
        for x, val in enumerate(row):
            print(Style.RESET_ALL, end='')
            if visited[y][x]:
                print(Back.RED + val, end='')
            elif [y, x] in to_visit:
                print(Back.GREEN + val, end='')
            else:
                print(Style.RESET_ALL + val, end='')
        print()


def solve(nodes, S_pos):
    x_dim, y_dim = len(nodes[0])-1, len(nodes)-1
    E_pos = find_pos(nodes, 'E')

    visited = [[0 for x in range(len(nodes[0]))] for l in range(len(nodes))]
    to_visit = []

    def check_nearby(current_node):
        x, y = current_node
        current_letter = nodes[x][y]
        current_weigth = visited[x][y]
        for node in [[x, y+1], [x, y-1], [x+1, y], [x-1, y]]:
            node_x, node_y = node
            if check_inside(node, x_dim, y_dim):
                next_letter = nodes[node_x][node_y]
                next_weigth = visited[node_x][node_y]
                if letter_reachable(current_letter, next_letter):
                    if next_weigth >= current_weigth+1 or next_weigth == 0:
                        visited[node_x][node_y] = current_weigth+1
                        if node not in to_visit:
                            to_visit.append((node))
                        # to_visit = set(to_visit)
                        # print(f'{next_letter} is reachable from current letter {current_letter}')
                # print(f'node {node[0]}, {node[1]} is inside')
        to_visit.pop(0)
    # initially check starting_point
    # from there to_visit gets filled by logic if node could be reached
    to_visit.append(S_pos)
    while to_visit:
        # print_maze(nodes, visited, to_visit)
        # sleep(.05)
        check_nearby(to_visit[0])

    print(f'Weight to reach E: {visited[E_pos[0]][E_pos[1]]}')
    return visited[E_pos[0]][E_pos[1]]


def main():
    input = open('day_12/input.txt', 'r')
    text_input = input.read().rstrip().split('\n')

    nodes = [[x for x in line] for line in text_input]
    S_pos = []
    S_pos.append(find_pos(nodes, 'S'))
    print(f'{S_pos}')
    # From Starting Point Check Node Top/Down/Left/Right vor visibility
    # If can be visited: Add to visited with Path Length

    # Part2: Append list of all a's as starting points
    a_s = find_all_pos(nodes, 'a')
    for a in a_s:
        S_pos.append(a)

    solutions = []

    for start in S_pos:
        solutions.append(solve(nodes, start))

    print(min(x if (x > 0) else 100000 for x in solutions))


if __name__ == "__main__":
    main()
