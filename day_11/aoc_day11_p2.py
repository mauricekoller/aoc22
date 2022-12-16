import math


def check_div(number, divisor):
    return 1 if not number % divisor else 0


def main():
    with open('day_11/ex_input.txt', 'r') as input:
        text_input = input.read().rstrip().split('\n\n')
        monkeys = {}
        rounds = 20

        for block in text_input:
            lines = block.splitlines()
            monkey_id = int(lines[0].split(' ')[1].split(':')[0])
            st, op, te, tr, fa = [x.split(': ')[1] for x in lines[1:]]
            monkeys[monkey_id] = {
                'items': list({'factors': set([int(x)]), 'additions': [0]} for x in st.split(', ')),
                'operation': [x for x in op.split(' ')[3:5]],
                'div_cond': int(te.split('by ')[1]),
                'if_true': int(tr.split(' ')[-1]),
                'if_false': int(fa.split(' ')[-1])
            }

        inspection_counter = [0 for _ in range(len(monkeys))]

        for _ in range(rounds):
            for monkey in range(len(monkeys)):
                operation = monkeys[monkey]['operation']
                div_cond = monkeys[monkey]['div_cond']
                if_true = monkeys[monkey]['if_true']
                if_false = monkeys[monkey]['if_false']
                items_to_pop = []
                for item in range(len(monkeys[monkey]['items'])):
                    curr_item = monkeys[monkey]['items'][item]
                    # increase inspection counter
                    inspection_counter[monkey] += 1
                    # apply operation
                    value_to_apply = (curr_item if operation[1] == 'old' else int(operation[1]))
                    if operation[0] == '+':
                        curr_item['additions'][0] += (value_to_apply)
                    elif operation[0] == '*':
                        curr_item['factors'].add(value_to_apply)
                    # Check if div_cond is in factors and additions are modulo div_cond:
                    if div_cond in curr_item['factors'] and not curr_item['additions'][0] % div_cond:
                        monkeys[if_true]['items'].append(curr_item)
                        items_to_pop.append(item)
                    else:
                        monkeys[if_false]['items'].append(curr_item)
                        items_to_pop.append(item)

                items_to_pop.reverse()
                for item in items_to_pop:
                    monkeys[monkey]['items'].pop(item)

        # inspection_counter.sort(reverse=True)
        print(f'Two most active Monkeys: {inspection_counter[0]} * {inspection_counter[1]} = {inspection_counter[0] * inspection_counter[1]}')


if __name__ == "__main__":
    main()
