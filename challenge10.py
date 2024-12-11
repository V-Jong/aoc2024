import time


def do_challenge():
    start_time = time.time()
    file = open('10/input.txt', 'r')
    lines = file.readlines()
    total = do_challenge_a(lines)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")
    print(f'Total: {total}')


def do_challenge_a(lines):
    total = 0
    digits = []
    for line_index, line in enumerate(lines):
        line_digits = []
        for c_index, c in enumerate(line):
            if c.isdigit():
                line_digits.append(Digit(int(c), c_index, line_index))
        digits.append(line_digits)

    lower_boundary = len(lines) - 1
    right_boundary = len(digits[0]) - 1
    flattened = [item for sublist in digits for item in sublist]
    flattened_dict = {(l.x, l.y): l for l in flattened}
    for digit_0 in [x for x in flattened if x.digit == 0]:
        print(f'Calculating score for 0 {digit_0}')
        reached_9 = set()
        count_path_to_9(digit_0, reached_9, right_boundary, lower_boundary, flattened_dict)
        score = len(reached_9)
        print(f'Score = {score}')
        total += score

    return total


class Digit:
    def __init__(self, digit, x, y):
        self.digit = digit
        self.x = x
        self.y = y

    def __str__(self):
        return f'Digit: {self.digit} ({self.x}, {self.y})'

    def __repr__(self):
        return f'Digit: {self.digit} ({self.x}, {self.y})'


def count_path_to_9(current_digit: Digit, reached_9: set, max_x: int, max_y: int, flattened_dict: dict):
    print(f'Checking current digit {current_digit}')
    if current_digit.digit == 9:
        reached_9.add(current_digit)
        return
    # process left and right
    target_digit = current_digit.digit + 1
    to_travel = []
    if current_digit.x >= 1:
        left_digit = flattened_dict.get((current_digit.x - 1, current_digit.y))
        if left_digit.digit == target_digit:
            to_travel.append(left_digit)
    if current_digit.x <= max_x - 1:
        right_digit = flattened_dict.get((current_digit.x + 1, current_digit.y))
        if right_digit.digit == target_digit:
            to_travel.append(right_digit)
    if current_digit.y >= 1:
        upper_digit = flattened_dict.get((current_digit.x, current_digit.y - 1))
        if upper_digit.digit == target_digit:
            to_travel.append(upper_digit)
    if current_digit.y <= max_y - 1:
        lower_digit = flattened_dict.get((current_digit.x, current_digit.y + 1))
        if lower_digit.digit == target_digit:
            to_travel.append(lower_digit)

    if len(to_travel) == 0:
        return

    for digit in to_travel:
        count_path_to_9(digit, reached_9, max_x, max_y, flattened_dict)
