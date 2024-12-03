import re


def do_challenge():
    file = open('3/input.txt', 'r')
    lines = file.readlines()
    total = do_challenge_a(lines)
    print(f'Total: {total}')


def do_challenge_a(lines):
    total = 0
    for line in lines:
        mults = re.findall(r'mul\(\d+,\d+\)', line)
        for mult in mults:
            digits = re.search(r'(\d+),(\d+)', mult)
            digit1 = int(digits.group(1))
            digit2 = int(digits.group(2))
            mul = digit1 * digit2
            total = total + mul
    return total
