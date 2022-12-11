def check_sprite(cycle_count, register):
    cycle_mod = cycle_count % 40
    if register in range(cycle_mod-1, cycle_mod+2):
        print('##', end='')
    else:
        print('..', end='')
    if cycle_count in [x for x in range(39, 240, 40)]:
        print()


def main():
    with open('day_10/input.txt', 'r') as input:
        text_lines = input.read().rstrip().splitlines()
        cycle_count = 0
        register = 1
        cycles = [20, 60, 100, 140, 180, 220]
        total_signal = 0

        for line in text_lines:
            if (line == 'noop'):
                check_sprite(cycle_count=cycle_count, register=register)
                cycle_count += 1
            else:
                value = int(line.split(' ')[1])
                for _ in range(2):
                    check_sprite(cycle_count=cycle_count, register=register)
                    cycle_count += 1
                register += value

        print(f'Total Signal_Strength: {total_signal}')


if __name__ == "__main__":
    main()
