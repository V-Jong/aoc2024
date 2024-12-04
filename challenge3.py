import re
import time


def do_challenge():
    start_time = time.time()
    file = open('3/input.txt', 'r')
    lines = file.read()
    total = do_challenge_a([lines])
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")
    print(f'Total: {total}')


def do_challenge_a(lines):
    total = 0
    pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"

    for line in lines:
        instructions_enabled = True
        matches = re.findall(pattern, line)

        for index, match in enumerate(matches):
            match_str = match
            # print(f'Evaluating match_str: {match_str}')

            if match_str.startswith("mul(") and instructions_enabled:
                digitsregex = re.findall(r'mul\((\d+),(\d+)\)', match_str)
                for digits in digitsregex:
                    digit1 = int(digits[0])
                    digit2 = int(digits[1])
                    # print(f'Should multiply {digit1} and {digit2}')
                    mul = digit1 * digit2
                    total = total + mul

            if match_str == "do()":
                # print(f'Found do(), enabling instructions')
                instructions_enabled = True
            elif match_str == "don't()":
                # print(f'Found don\'t(), disabling instructions')
                instructions_enabled = False

    return total
