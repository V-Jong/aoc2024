import time
from itertools import combinations


def do_challenge():
    start_time = time.time()
    file = open('8/input.txt', 'r')
    lines = file.readlines()
    total = do_challenge_a(lines)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")
    print(f'Total: {total}')


def do_challenge_a(lines):
    letters = []
    min_x = 0
    min_y = 0
    max_x = 0
    max_y = len(lines) - 1
    for line_index, line in enumerate(lines):
        max_x = len(line) - 1
        line_letters = []
        for c_index, c in enumerate(line):
            if c.isalnum():
                line_letters.append(Letter(c, c_index, line_index))
        letters.append(line_letters)

    flattened = [item for sublist in letters for item in sublist]
    distinct_letters = list(set([letter.character for letter in flattened]))

    antinodes = set()
    for distinct_letter in distinct_letters:
        sub_flattened = [letter for letter in flattened if letter.character == distinct_letter]
        sub_combs = list(combinations(sub_flattened, 2))
        for sub_comb in sub_combs:
            pair_1 = sub_comb[0]
            pair_2 = sub_comb[1]
            p1_x = pair_1.x
            p1_y = pair_1.y
            p2_x = pair_2.x
            p2_y = pair_2.y
            if p1_x == p2_x:
                y_dist = abs(p1_y - p2_y)
                if p1_y < p2_y:
                    antinode1 = (p1_x, p1_y - y_dist)
                    antinode2 = (p1_x, p2_y + y_dist)
                else:
                    antinode1 = (p1_x, p2_y - y_dist)
                    antinode2 = (p1_x, p1_y + y_dist)
            elif p1_y == p2_y:
                x_dist = abs(p1_x - p2_x)
                if p1_x < p2_x:
                    antinode1 = (p1_x - x_dist, p1_y)
                    antinode2 = (p2_x + x_dist, p1_y)
                else:
                    antinode1 = (p1_x + x_dist, p1_y)
                    antinode2 = (p2_x - x_dist, p1_y)
            elif p1_x < p2_x:
                x_dist = abs(p1_x - p2_x)
                y_dist = abs(p1_y - p2_y)
                if p1_y < p2_y:
                    antinode1 = (p1_x - x_dist, p1_y - y_dist)
                    antinode2 = (p2_x + x_dist, p2_y + y_dist)
                else:
                    antinode1 = (p1_x - x_dist, p1_y + y_dist)
                    antinode2 = (p2_x + x_dist, p2_y - y_dist)
            else:
                x_dist = abs(p1_x - p2_x)
                y_dist = abs(p1_y - p2_y)
                if p1_y < p2_y:
                    antinode1 = (p1_x + x_dist, p1_y - y_dist)
                    antinode2 = (p2_x - x_dist, p2_y + y_dist)
                else:
                    antinode1 = (p1_x + x_dist, p1_y + y_dist)
                    antinode2 = (p2_x - x_dist, p2_y - y_dist)

            if antinode1 != (0, 0) and min_x <= antinode1[0] <= max_x and min_y <= antinode1[1] <= max_y:
                antinodes.add(antinode1)
            if antinode2 != (0, 0) and min_x <= antinode2[0] <= max_x and min_y <= antinode2[1] <= max_y:
                antinodes.add(antinode2)

    return len(antinodes)


def do_challenge_b(lines):
    total = 0
    return total


class Letter:
    def __init__(self, character, x, y):
        self.character = character
        self.x = x
        self.y = y

    def __str__(self):
        return f'Letter: {self.character} ({self.x}, {self.y})'

    def __repr__(self):
        return f'Letter: {self.character} ({self.x}, {self.y})'