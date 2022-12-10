# def sum_subdirs(dir):
#     return_size = 0
#     subdirs = fs[dir]['childnodes']
#     if subdirs:
#         for subdir in subdirs:
#             # return_size += fs[subdir]['dir_size']
#             subsubdirs = fs[subdir]['childnodes']
#             if subsubdirs:
#                 for subsubdir in subsubdirs:
#                     return_size += sum_subdirs(subsubdir)
#    return return_size


def find_closest_dir(fs, size):
    fs_size = 70000000
    free_up_size = size - (fs_size - fs['/']['dir_size'])
    closest_dir = ''
    closest_dir_size = fs_size
    for dir in fs:
        dir_size = fs[dir]['dir_size']
        if dir_size >= free_up_size and dir_size <= closest_dir_size:
            closest_dir = dir
            closest_dir_size = dir_size
    return closest_dir_size


def move_up_in_tree(fs, nodes):
    new_dirs = []
    for dir in nodes:
        parent_dir = fs[dir]['parent_dir'][0]
        # Calculate Parent_Dir and update in fs
        parent_dir_size = 0
        # Add all childnodes
        for childnode in fs[parent_dir]['childnodes']:
            parent_dir_size += fs[childnode]['dir_size']
        # Add all files in parent_dir
        for file in fs[parent_dir]['files']:
            parent_dir_size += int(file['size'])

        # Check if dir_size in fs is smaller than new value
        if fs[parent_dir]['dir_size'] < parent_dir_size:
            fs[parent_dir]['dir_size'] = parent_dir_size

        if (parent_dir != '/'):
            new_dirs.append(parent_dir)

    if new_dirs:
        fs = move_up_in_tree(fs, set(new_dirs))

    return fs


def recalculate_final_tree(fs):
    tree_size = 0
    final_nodes = {key: value for (key, value) in fs.items() if value['childnodes'] == []}
    print(final_nodes)
    move_up_in_tree(fs, final_nodes)

    return fs


with open('Day7/input.txt', 'r') as input:
    text = input.read().rstrip()
    text = text.splitlines()

    current_dir = ''

    fs = {'/': {'parent_dir': [], 'childnodes': [], 'files': [], 'dir_size': 0}}

    for line in text:
        split_line = line.split(' ')
        if split_line[0] == '$':
            command = split_line[1]
            if command == 'cd':
                cd = split_line[2]
                if cd == '..':
                    current_dir = current_dir.rsplit('/', 1)[0]
                elif cd == '/':
                    current_dir = cd
                else:
                    if current_dir == '/':
                        current_dir += f'{cd}'
                    else:
                        current_dir += f'/{cd}'
            elif command == 'ls':
                pass
        else:
            # check if dir or filesize
            if split_line[0] == 'dir':
                dir = split_line[1]
                if current_dir == '/':
                    new_dir = f'{current_dir}{dir}'
                else:
                    new_dir = f'{current_dir}/{dir}'
                fs[current_dir]['childnodes'].append(new_dir)
                fs[new_dir] = {'parent_dir': [current_dir], 'childnodes': [], 'files': [], 'dir_size': 0}
            else:
                filesize = split_line[0]
                filename = split_line[1]
                fs[current_dir]['files'].append({'filename': filename, 'size': filesize})
                fs[current_dir]['dir_size'] += int(filesize)

    total_size_of_small_dirs = 0
    recalculated_fs = recalculate_final_tree(fs)
    for entry in recalculated_fs:
        dir = entry
        dir_size = fs[entry]['dir_size']
        # Loop over all subdirs and add their size
        # dir_size += sum_subdirs(entry)

        if dir_size <= 100000:
            total_size_of_small_dirs += dir_size
            print(f'{dir} size: {dir_size}')
    print(f'Total size of all small dirs: {total_size_of_small_dirs}')
    print(f'Directory to delete has size {find_closest_dir(fs,30000000)}')
