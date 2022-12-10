def abspath(dir_list):
    return '/'.join(dir_list)


def find_closest_dir(fs, size):
    fs_size = 70000000
    free_up_size = size - (fs_size - fs['root']['dir_size'])
    closest_dir = ''
    closest_dir_size = fs_size
    for dir in fs:
        dir_size = fs[dir]['dir_size']
        if dir_size >= free_up_size and dir_size <= closest_dir_size:
            closest_dir = dir
            closest_dir_size = dir_size
    return closest_dir_size


with open('Day7/input.txt', 'r') as input:
    text = input.read().rstrip().splitlines()

    current_dir = []

    fs = {'root': {'parent_dir': [], 'childnodes': [], 'files': [], 'dir_size': 0}}

    for line in text:
        split_line = line.split(' ')
        if split_line[0] == '$':
            command = split_line[1]
            if command == 'cd':
                cd = split_line[2]
                if cd == '..':
                    current_dir.pop()
                elif cd == '/':
                    current_dir = ['root']
                else:
                    current_dir.append(cd)
        else:
            # check if dir or filesize
            if split_line[0] == 'dir':
                dir = split_line[1]
                new_dir = abspath(current_dir+[dir])
                fs[abspath(current_dir)]['childnodes'].append(new_dir)
                fs[new_dir] = {'parent_dir': [abspath(current_dir)], 'childnodes': [], 'files': [], 'dir_size': 0}
            else:
                filesize, filename = [split_line[i] for i in (0, 1)]
                fs[abspath(current_dir)]['files'].append({'filename': filename, 'size': filesize})
                fs[abspath(current_dir)]['dir_size'] += int(filesize)
                # Update Filesize for all parent dirs
                for i in range(1, len(current_dir)):
                    update_dir = abspath(current_dir[:i])
                    fs[update_dir]['dir_size'] += int(filesize)

    total_size_of_small_dirs = 0
    for dir in fs:
        if fs[dir]['dir_size'] <= 100000:
            total_size_of_small_dirs += fs[dir]['dir_size']
    print(f'Total size of all small dirs: {total_size_of_small_dirs}')
    print(f'Directory to delete has size {find_closest_dir(fs,30000000)}')
