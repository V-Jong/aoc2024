from enum import Enum


def do_challenge():
    file = open('2/test.txt', 'r')
    lines = file.readlines()
    total = do_challenge_a(lines)
    print(f'Total: {total}')


def do_challenge_a(lines):
    safe = 0
    levels_list = []
    for line in lines:
        line = line.replace('\n', '')
        levels_split = line.split(' ')
        levels = []
        for level_str in levels_split:
            levels.append(int(level_str))
        levels_list.append(levels)
    for index, levels in enumerate(levels_list):
        trend = Trend.INCREASING
        if levels[0] > levels[1]:
            trend = Trend.DECREASING
        level_safe = is_level_safe(levels, trend)
        if level_safe:
            safe = safe + 1
    return safe


def is_level_safe(levels, trend):
    level_safe = False
    for l_index, level in enumerate(levels):
        # print(f'At l index {l_index} with len {len(levels)}, current level {level}')
        if l_index == (len(levels) - 1):
            # print(f'Continuing')
            continue
        second_n = levels[l_index + 1]
        is_this_level_safe = is_safe(level, second_n, trend)
        print(f'Evaluating levels {level} and next {second_n}, increasing {trend}; result {is_this_level_safe}')
        if not is_this_level_safe:
            print(f'Not safe, stopping')
            break
        if l_index == len(levels) - 2:
            print(f'Setting this level to safe')
            level_safe = True
    return level_safe


def is_safe(level1, level2, trend):
    abs_diff = abs(level1 - level2)
    valid_trend = False
    if trend == Trend.INCREASING and level2 > level1:
        valid_trend = True
    if trend == Trend.DECREASING and level2 < level1:
        valid_trend = True
    print(f'Checking first {level1}, second {level2}; diff {abs_diff} and trend {trend} is valid {valid_trend}')
    return 1 <= abs_diff <= 3 and valid_trend


class Trend(Enum):
    INCREASING = 1
    DECREASING = 2
