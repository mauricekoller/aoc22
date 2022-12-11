def return_signal(cycle_count, register):
    current_signal = cycle_count * register
    print(f'Current Signal at Cycle {cycle_count} * {register}: {current_signal}')
    return current_signal


def main():
    with open('day_10/input.txt', 'r') as input:
        text_lines = input.read().rstrip().splitlines()
        cycle_count = 0
        register = 1
        cycles = [20, 60, 100, 140, 180, 220]
        total_signal = 0

        for line in text_lines:
            if cycle_count in cycles:
                cycles.pop(0)
                total_signal += return_signal(cycle_count=cycle_count, register=register)
            if (line == 'noop'):
                cycle_count += 1
            else:
                value = int(line.split(' ')[1])
                for _ in range(2):
                    cycle_count += 1
                    if cycle_count in cycles:
                        cycles.pop(0)
                        total_signal += return_signal(cycle_count=cycle_count, register=register)
                register += value

        print(f'Total Signal_Strength: {total_signal}')


if __name__ == "__main__":
    main()
