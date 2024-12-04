import re


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

    upper_boundary = 0
    lower_boundary = len(lines) - 1
    left_boundary = 0
    right_boundary = len(letters[0]) - 1
    valid_additional = 'MAS'
    # print(f'Lower b: {lower_boundary}, right b: {right_boundary}')
    flattened = [item for sublist in letters for item in sublist]
    for letter in [x for x in flattened if x.character == 'X']:
        valid_xmas = False
        # print('')
        # print(f'Found X: {letter}')
        # Get 3 letters hor right
        if abs(letter.x - right_boundary) >= 3:
            r_name = get_additional_letters_hor(letter.y, letter.x + 1, letter.x + 2, letter.x + 3, flattened)
            if r_name == valid_additional:
                # print(f'Valid check right')
                total = total + 1
            if abs(letter.y - lower_boundary) >= 3:
                r_name = get_additional_letters_hor_ver(letter.y + 1, letter.y + 2, letter.y + 3, letter.x + 1,
                                                        letter.x + 2, letter.x + 3, flattened)
                if r_name == valid_additional:
                    # print(f'Valid check down right')
                    total = total + 1
            if abs(letter.y - upper_boundary) >= 3:
                r_name = get_additional_letters_hor_ver(letter.y - 1, letter.y - 2, letter.y - 3, letter.x + 1,
                                                        letter.x + 2, letter.x + 3, flattened)
                r_name = r_name[::-1]
                # print(f'Found top right name: {r_name}')
                if r_name == valid_additional:
                    # print(f'Valid check up right')
                    total = total + 1
        # Get 3 letters hor left
        if abs(letter.x - left_boundary) >= 3:
            r_name = get_additional_letters_hor(letter.y, letter.x - 3, letter.x - 2, letter.x - 1, flattened)
            r_name = r_name[::-1]
            if r_name == valid_additional:
                # print(f'Valid check left')
                total = total + 1
            if abs(letter.y - lower_boundary) >= 3:
                r_name = get_additional_letters_hor_ver(letter.y + 1, letter.y + 2, letter.y + 3, letter.x - 1,
                                                        letter.x - 2, letter.x - 3, flattened)
                # r_name = r_name[::-1]
                # print(f'Found down left name: {r_name}')
                if r_name == valid_additional:
                    # print(f'Valid check down left')
                    total = total + 1
            if abs(letter.y - upper_boundary) >= 3:
                r_name = get_additional_letters_hor_ver(letter.y - 1, letter.y - 2, letter.y - 3, letter.x - 1,
                                                        letter.x - 2, letter.x - 3, flattened)
                r_name = r_name[::-1]
                if r_name == valid_additional:
                    # print(f'Valid check up left')
                    total = total + 1
        # Get 3 letters ver down
        if abs(letter.y - lower_boundary) >= 3:
            r_name = get_additional_letters_ver(letter.x, letter.y + 1, letter.y + 2, letter.y + 3, flattened)
            if r_name == valid_additional:
                # print(f'Valid check down')
                total = total + 1
        # Get 3 letters ver up
        if abs(letter.y - upper_boundary) >= 3:
            r_name = get_additional_letters_ver(letter.x, letter.y - 1, letter.y - 2, letter.y - 3, flattened)
            r_name = r_name[::-1]
            # print(f'Found up name: {r_name}')
            if r_name == valid_additional:
                # print(f'Valid check up')
                total = total + 1

        # if valid_xmas:
        #     print(f'Valid XMAS at: {letter}')

    return total


def get_additional_letters_hor(y, x1, x2, x3, list):
    r_letters = [l for l in list if l.y == y and (l.x == x1 or l.x == x2 or l.x == x3)]
    return "".join(l.character for l in r_letters)


def get_additional_letters_ver(x, y1, y2, y3, list):
    r_letters = [l for l in list if l.x == x and (l.y == y1 or l.y == y2 or l.y == y3)]
    return "".join(l.character for l in r_letters)


def get_additional_letters_hor_ver(y1, y2, y3, x1, x2, x3, list):
    r_letters = [l for l in list if (l.y == y1 and l.x == x1) or (l.y == y2 and l.x == x2) or (l.y == y3 and l.x == x3)]
    return "".join(l.character for l in r_letters)


class Letter:
    def __init__(self, character, x, y):
        self.character = character
        self.x = x
        self.y = y

    def __str__(self):
        return f'Letter: {self.character} and x: ({self.x}), y: {self.y}'

    def __repr__(self):
        return f'Letter: {self.character} and x: ({self.x}), y: {self.y}'
