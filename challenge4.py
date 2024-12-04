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

    look_head_limit = 2
    upper_boundary = 0
    lower_boundary = len(lines) - 1
    left_boundary = 0
    right_boundary = len(letters[0]) - 1
    valid_additional = 'AS'
    checked_m = []
    # print(f'Lower b: {lower_boundary}, right b: {right_boundary}')
    flattened = [item for sublist in letters for item in sublist]
    start_time = time.time()
    for letter in [x for x in flattened if x.character == 'M']:
        print('')
        print(f'Found X: {letter}')
        print(f'Checked Ms: {checked_m}')
        if abs(letter.x - right_boundary) >= look_head_limit:
            if abs(letter.y - lower_boundary) >= look_head_limit:
                r_name = get_additional_letters_hor_ver(letter.y + 1, letter.y + 2, letter.x + 1, letter.x + 2,
                                                        flattened)
                if r_name == valid_additional:
                    # print(f'Valid check down right')
                    # Check if there is an X with MAS
                    letter_a = [l for l in flattened
                                if l.character == 'A' and l.x == letter.x + 1 and l.y == letter.y + 1][0]
                    print(f'Found letter A at {letter_a}')
                    # Check M at top right and S at bottom left
                    letter_m = [l for l in flattened if l.y == letter_a.y - 1 and l.x == letter_a.x + 1]
                    if valid_mas_for_a(letter_m, letter_a.x - 1, letter_a.y + 1, flattened, checked_m, letter_a):
                        print(f'Valid MAS, adding A {letter_a}')
                        checked_m.append(letter_a)
                        total = total + 1
                    # Check M at bottom left and S at top right
                    letter_m = [l for l in flattened if l.y == letter_a.y + 1 and l.x == letter_a.x - 1]
                    if valid_mas_for_a(letter_m, letter_a.x + 1, letter_a.y - 1, flattened, checked_m, letter_a):
                        print(f'Valid MAS, adding A {letter_a}')
                        checked_m.append(letter_a)
                        total = total + 1
            if abs(letter.y - upper_boundary) >= look_head_limit:
                r_name = get_additional_letters_hor_ver(letter.y - 1, letter.y - 2, letter.x + 1, letter.x + 2,
                                                        flattened)
                r_name = r_name[::-1]
                # print(f'Found top right name: {r_name}')
                if r_name == valid_additional:
                    # print(f'Valid check up right')
                    # Check if there is an X with MAS
                    letter_a = [l for l in flattened
                                if l.character == 'A' and l.x == letter.x + 1 and l.y == letter.y - 1][0]
                    print(f'Found letter A at {letter_a}')
                    # Check M at top left and S at bottom right
                    letter_m = [l for l in flattened if l.y == letter_a.y - 1 and l.x == letter_a.x - 1]
                    if valid_mas_for_a(letter_m, letter_a.x + 1, letter_a.y + 1, flattened, checked_m, letter_a):
                        print(f'Valid MAS, adding A {letter_a}')
                        checked_m.append(letter_a)
                        total = total + 1
                    # Check M at bottom right and S at top left
                    letter_m = [l for l in flattened if l.y == letter_a.y + 1 and l.x == letter_a.x + 1]
                    if valid_mas_for_a(letter_m, letter_a.x - 1, letter_a.y - 1, flattened, checked_m, letter_a):
                        print(f'Valid MAS, adding A {letter_a}')
                        checked_m.append(letter_a)
                        total = total + 1
        if abs(letter.x - left_boundary) >= look_head_limit:
            if abs(letter.y - lower_boundary) >= look_head_limit:
                r_name = get_additional_letters_hor_ver(letter.y + 1, letter.y + 2, letter.x - 1, letter.x - 2,
                                                        flattened)
                # r_name = r_name[::-1]
                # print(f'Found down left name: {r_name}')
                if r_name == valid_additional:
                    # print(f'Valid check down left')
                    # Check if there is an X with MAS
                    letter_a = [l for l in flattened
                                if l.character == 'A' and l.x == letter.x - 1 and l.y == letter.y + 1][0]
                    print(f'Found letter A at {letter_a}')
                    # Check M at top left and S at bottom right
                    letter_m = [l for l in flattened if l.y == letter_a.y - 1 and l.x == letter_a.x - 1]
                    if valid_mas_for_a(letter_m, letter_a.x + 1, letter_a.y + 1, flattened, checked_m, letter_a):
                        # print(f'Valid MAS, adding A {letter_a}')
                        checked_m.append(letter_a)
                        total = total + 1
                    # Check M at bottom right and S at top left
                    letter_m = [l for l in flattened if l.y == letter_a.y + 1 and l.x == letter_a.x + 1]
                    if valid_mas_for_a(letter_m, letter_a.x - 1, letter_a.y - 1, flattened, checked_m, letter_a):
                        # print(f'Valid MAS, adding A {letter_a}')
                        checked_m.append(letter_a)
                        total = total + 1
            if abs(letter.y - upper_boundary) >= look_head_limit:
                r_name = get_additional_letters_hor_ver(letter.y - 1, letter.y - 2, letter.x - 1, letter.x - 2,
                                                        flattened)
                r_name = r_name[::-1]
                if r_name == valid_additional:
                    # print(f'Valid check up left')
                    # Check if there is an X with MAS
                    letter_a = [l for l in flattened
                                if l.character == 'A' and l.x == letter.x - 1 and l.y == letter.y - 1][0]
                    print(f'Found letter A at {letter_a}')
                    # Check M at top right and S at bottom left
                    letter_m = [l for l in flattened if l.y == letter_a.y - 1 and l.x == letter_a.x + 1]
                    if valid_mas_for_a(letter_m, letter_a.x - 1, letter_a.y + 1, flattened, checked_m, letter_a):
                        # print(f'Valid MAS, adding A {letter_a}')
                        checked_m.append(letter_a)
                        total = total + 1
                    # Check M at bottom left and S at top right
                    letter_m = [l for l in flattened if l.y == letter_a.y + 1 and l.x == letter_a.x - 1]
                    if valid_mas_for_a(letter_m, letter_a.x + 1, letter_a.y - 1, flattened, checked_m, letter_a):
                        # print(f'Valid MAS, adding A {letter_a}')
                        checked_m.append(letter_a)
                        total = total + 1
    print(f'Known Ms ({len(checked_m)}): {checked_m}')

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
