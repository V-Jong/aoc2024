import time
from itertools import product


def do_challenge():
    start_time = time.time()
    file = open('7/input.txt', 'r')
    lines = file.readlines()
    total = do_challenge_a(lines)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")
    print(f'Total: {total}')


def do_challenge_a(lines):
    total = 0
    allowed_operators = ['+', '*']

    for line in lines:
        line_goal_split = line.split(':')
        goal = int(line_goal_split[0])
        numbers = [int(number) for number in line_goal_split[1].strip().split(' ')]
        possible_operator_combinations = list(product(allowed_operators, repeat=len(numbers) - 1))
        # print(f'Goal {goal} with numbers {numbers}')
        # print(f'Combinations of ops {possible_operator_combinations}')
        valid_combination_found = False
        for combination in possible_operator_combinations:
            # print()
            # print(f'Using combination {combination}')
            c_numbers = numbers.copy()
            while len(c_numbers) != 1:
                for operator in combination:
                    # print(f'Using operator: {operator} on {c_numbers}')
                    number1 = c_numbers[0]
                    number2 = c_numbers[1]
                    res = 0
                    if operator == '+':
                        res = number1 + number2
                    elif operator == '*':
                        res = number1 * number2
                    c_numbers.pop(0)
                    c_numbers.pop(0)
                    c_numbers.insert(0, res)
                    # print(f'Calculating with new numbers {c_numbers}')
            if goal == c_numbers[0]:
                valid_combination_found = True
        if valid_combination_found:
            # print(f'Found valid combination')
            total += goal

    return total
