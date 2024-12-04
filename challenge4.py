import re
import time


def do_challenge():
    file = open('4/input.txt', 'r')
    lines = file.readlines()
    total = do_challenge_a(lines)
    print(f'Total: {total}')


def do_challenge_a(lines):
    total = 0
    letters = []
    for line_index, line in enumerate(lines):
        letter_matches = [char for char in line if char.isalpha()]
        line_letters = []
        for c_index, c in enumerate(letter_matches):
            line_letters.append(Letter(c, c_index, line_index))
        # print(f'Found letters on line {line_index}: {line_letters}')
        letters.append(line_letters)

    look_head_limit = 1
    upper_boundary = 0
    lower_boundary = len(lines) - 1
    left_boundary = 0
    right_boundary = len(letters[0]) - 1
    valid_additional = 'AS'
    checked_m = []
    # print(f'Lower b: {lower_boundary}, right b: {right_boundary}')
    flattened = [item for sublist in letters for item in sublist]
    start_time = time.time()
    for letter_a in [x for x in flattened if x.character == 'A']:
        # print('')
        # print(f'Found A: {letter_a}')
        # print(f'Checked Ms: {checked_m}')
        if (abs(letter_a.x - right_boundary) >= look_head_limit and abs(letter_a.x - left_boundary) >= look_head_limit and
                abs(letter_a.y - lower_boundary) >= look_head_limit and abs(letter_a.y - upper_boundary) >= look_head_limit):
            top_left = [l for l in flattened if l.y == letter_a.y - 1 and l.x == letter_a.x - 1][0]
            top_right = [l for l in flattened if l.y == letter_a.y - 1 and l.x == letter_a.x + 1][0]
            bottom_left = [l for l in flattened if l.y == letter_a.y + 1 and l.x == letter_a.x - 1][0]
            bottom_right = [l for l in flattened if l.y == letter_a.y + 1 and l.x == letter_a.x + 1][0]
            # print(f'Top left: {top_left}')
            # print(f'Top right: {top_right}')
            # print(f'Bottom left: {bottom_left}')
            # print(f'Bottom right: {bottom_right}')

            top_side_m = (top_left.character == top_right.character and bottom_left.character == bottom_right.character
                           and top_left.character == 'M' and bottom_left.character == 'S')
            bottom_side_m = (top_left.character == top_right.character and bottom_left.character == bottom_right.character
                          and top_left.character == 'S' and bottom_left.character == 'M')
            left_side_m = (top_left.character == bottom_left.character and top_right.character == bottom_right.character
                           and top_left.character == 'M' and top_right.character == 'S')
            right_side_m = (top_left.character == bottom_left.character and top_right.character == bottom_right.character
                           and top_left.character == 'S' and top_right.character == 'M')
            # print(f'Top side m and bottom s: {top_side_m}')
            # print(f'Top side s and bottom m: {bottom_side_m}')
            # print(f'Left side m and right s: {left_side_m}')
            # print(f'Left side s and right m: {right_side_m}')
            if top_side_m or bottom_side_m or left_side_m or right_side_m:
                # print(f'Valid MAS, adding A {letter_a}')
                checked_m.append(letter_a)
                total = total + 1
    # print(f'Known Ms ({len(checked_m)}): {checked_m}')

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")
    return total


def get_additional_letters_hor(y, x1, x2, x3, search_list):
    r_letters = [l for l in search_list if l.y == y and (l.x == x1 or l.x == x2 or l.x == x3)]
    return "".join(l.character for l in r_letters)


def get_additional_letters_ver(x, y1, y2, y3, search_list):
    r_letters = [l for l in search_list if l.x == x and (l.y == y1 or l.y == y2 or l.y == y3)]
    return "".join(l.character for l in r_letters)


def get_additional_letters_hor_ver(y1, y2, x1, x2, search_list):
    r_letters = [l for l in search_list if (l.y == y1 and l.x == x1) or (l.y == y2 and l.x == x2)]
    return "".join(l.character for l in r_letters)


def valid_mas_for_a(letter_m, x2, y2, search_list, known_list, letter_a):
    letter_s = [l for l in search_list if l.y == y2 and l.x == x2]
    known_a = any(l.x == letter_a.x and l.y == letter_a.y for l in known_list)
    print(f'Found mas for a: M {letter_m[0]} and S {letter_s}. A known = {known_a}')
    return not known_a and len(letter_m) == 1 and len(letter_s) == 1 and letter_m[0].character == 'M' and letter_s[0].character == 'S'


class Letter:
    def __init__(self, character, x, y):
        self.character = character
        self.x = x
        self.y = y

    def __str__(self):
        return f'Letter: {self.character} ({self.x}, {self.y})'

    def __repr__(self):
        return f'Letter: {self.character} ({self.x}, {self.y})'
