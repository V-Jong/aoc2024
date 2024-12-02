from enum import Enum


def do_challenge():
    file = open('2/input.txt', 'r')
    lines = file.readlines()
    total = do_challenge_a(lines)
    print(f'Total: {total}')


def do_challenge_a(lines):
    safe = 0
    levels_list = []
    unsafe_list = []
    for line in lines:
        line = line.replace('\n', '')
        levels_split = line.split(' ')
        levels = []
        for level_str in levels_split:
            levels.append(int(level_str))
        levels_list.append(levels)
    for index, levels in enumerate(levels_list):
        print(f'')
        print(f'Checking level at index {index}: {levels}')
        trend = Trend.INCREASING
        if levels[0] > levels[1]:
            trend = Trend.DECREASING
        level_safe = is_level_safe(levels, trend)
        if level_safe:
            safe = safe + 1
        else:
            unsafe_list.append(levels)
    for index, levels in enumerate(unsafe_list):
        for c_index, value in enumerate(levels):
            n_levels = list(levels)
            # print(f'Not safe, but checking if safe by removing pos {c_index}, value {value}.')
            n_levels.pop(c_index)
            # print(f'Now checking {n_levels}')
            trend = Trend.INCREASING
            if n_levels[0] > n_levels[1]:
                trend = Trend.DECREASING
            is_n_levels_safe = is_level_safe(n_levels, trend)
            if is_n_levels_safe:
                safe = safe + 1
                break
    return safe


def is_level_safe(levels, trend):
    level_safe = False
    for l_index, level in enumerate(levels):
        # print(f'At l index {l_index} with len {len(levels)}, current level {level}')
        if l_index == (len(levels) - 1):
            # print(f'Continuing')
            continue
        second_n = levels[l_index + 1]
        levels_diff_allowed = is_allowed_difference(level, second_n)
        levels_trend_allowed = is_valid_trend(level, second_n, trend)
        are_two_levels_safe = levels_diff_allowed and levels_trend_allowed
        print(f'Evaluating levels {level} and next {second_n}, increasing {trend}; result {are_two_levels_safe}')
        if not are_two_levels_safe:
            print(f'Not safe, stopping')
            break
        if l_index == len(levels) - 2:
            print(f'Setting this level to safe')
            level_safe = True
    return level_safe


def is_allowed_difference(level1, level2):
    abs_diff = abs(level1 - level2)
    print(f'Checking first {level1}, second {level2}; diff {abs_diff} ')
    return 1 <= abs_diff <= 3


def is_valid_trend(level1, level2, trend):
    valid_trend = False
    if trend == Trend.INCREASING and level2 > level1:
        valid_trend = True
    if trend == Trend.DECREASING and level2 < level1:
        valid_trend = True
    print(f'Checking first {level1}, second {level2}; trend {trend} is valid {valid_trend}')
    return valid_trend


class Trend(Enum):
    INCREASING = 1
    DECREASING = 2
