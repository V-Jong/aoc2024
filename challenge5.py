import time
from math import floor

enable_log = False


def do_challenge():
    file = open('5/input.txt', 'r')
    lines = file.read().splitlines()
    start_time = time.time()
    total = do_challenge_b(lines)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")
    print(f'Total: {total}')


def do_challenge_a(lines):
    total = 0
    rules = []
    updates = []
    for line_index, line in enumerate(lines):
        if len(line) == 0:
            continue
        if len(line) == 5:
            digits_str = line.split('|')
            rules.append((int(digits_str[0]), int(digits_str[1])))
        else:
            digits_str = line.split(',')
            updates.append(list(map(int, digits_str)))

    if enable_log:
        print(f'Found rules {rules}')
        print(f'Found updates {updates}')

    for update in updates:
        if enable_log:
            print(f'')
        valid_rules_for_update = True
        applicable_rules = [r for r in rules if r[0] in update and r[1] in update]
        if enable_log:
            print(f'Applicable rules for {update}: {applicable_rules}')
        for digit in update:
            rules_for_digit = [rule for rule in applicable_rules if digit in rule]
            valid_rules_for_update = (valid_rules_for_update and
                                      all(is_valid_rule_for_digit(digit, rule, update) for rule in rules_for_digit))
        if valid_rules_for_update:
            middle_digit = update[floor(len(update) / 2)]
            if enable_log:
                print(f'Adding middle {middle_digit}')
            total = total + middle_digit

    return total


def do_challenge_b(lines):
    total = 0
    rules = []
    updates = []
    for line_index, line in enumerate(lines):
        if len(line) == 0:
            continue
        if len(line) == 5:
            digits_str = line.split('|')
            rules.append((int(digits_str[0]), int(digits_str[1])))
        else:
            digits_str = line.split(',')
            updates.append(list(map(int, digits_str)))

    if enable_log:
        print(f'Found rules {rules}')
        print(f'Found updates {updates}')

    for index, update in enumerate(updates):
        if enable_log:
            print(f'')
            print(f'Update at index {index}')
        applicable_rules = [r for r in rules if r[0] in update and r[1] in update]
        rules_broken = set()
        if enable_log:
            print(f'Applicable rules for {update}: {applicable_rules}')
        valid_rules_for_update = are_valid_rules(update, applicable_rules, rules_broken)
        if not valid_rules_for_update:
            # Fix update
            if enable_log:
                print(f'')
                print(f'Fixing update: {update}')

            digit_ranking = {digit: 0 for digit in update}
            if enable_log:
                print(f'first digit ranking: {digit_ranking}')
            for digit in update:
                all_first_in_rules = [t[0] for t in applicable_rules]
                if enable_log:
                    print(f'all firsts: {all_first_in_rules}')
                digit_count = all_first_in_rules.count(digit)
                digit_ranking[digit] = digit_count
            if enable_log:
                print(f'new digit ranking: {digit_ranking}')
            fixed_as_list = [key for key, value in sorted(digit_ranking.items(), key=lambda item: item[1], reverse=True)]
            if enable_log:
                print(f'fixed: {fixed_as_list}')

            middle_digit = fixed_as_list[floor(len(fixed_as_list) / 2)]
            if enable_log:
                print(f'Adding middle {middle_digit}')
            total = total + middle_digit

    return total


def are_valid_rules(update, applicable_rules, rules_broken):
    valid_rules_for_update = True
    for digit in update:
        rules_for_digit = [rule for rule in applicable_rules if digit in rule]
        for rule in rules_for_digit:
            valid_rule = is_valid_rule_for_digit(digit, rule, update)
            if not valid_rule:
                rules_broken.add(rule)
            valid_rules_for_update = valid_rules_for_update and valid_rule
    return valid_rules_for_update


def is_valid_rule_for_digit(digit, rule, update):
    if digit == rule[0]:
        other = rule[1]
        res = update.index(digit) < update.index(other)
        # if enable_log:
        #     print(f'Checking rule {rule} if {digit} is before {other} = {res}')
        return res
    else:
        other = rule[0]
        res = update.index(digit) > update.index(other)
        # if enable_log:
        #     print(f'Checking rule {rule} if {digit} is after {other} = {res}')
        return res
