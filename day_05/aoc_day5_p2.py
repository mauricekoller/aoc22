with open('day_05/input.txt', 'r') as input:
    text = input.read().rstrip()
    # Split Input file into List of Containers and list of operations to be executed
    containers, operations = [object.splitlines() for object in text.split('\n\n')]
    # Determine length of Container by splitting the last line apart, seperating by whitespace and splitting the last number
    container_len = ''.join(containers[-1:])
    container_len = int(container_len.rsplit('   ', 1)[-1:][0])
    containers = containers[:-1]
    chars_per_line = container_len*4 - 1

    container_array = []

    for container in range(container_len):
        # container_array.append()
        stack = []
        # iterate from bottom to top through container list
        for row in reversed(containers):
            element = row[1 + container*4]
            if element != ' ':
                stack.append(element)
        container_array.append(stack)

    # Carry out all operations
    for operation in operations:
        quantity, container_from, container_to = operation.split(' ')[1::2]
        elements_to_move = []
        for i in range(int(quantity)):
            element_to_move = container_array[int(container_from)-1].pop()
            elements_to_move.append(element_to_move)
        container_array[int(container_to)-1].extend(elements_to_move[::-1])

    # Concat all Top Elements
    result = ''.join(container[-1] for container in container_array)

    print(f'Result: {result}')
