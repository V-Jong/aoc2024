import time


def do_challenge():
    start_time = time.time()
    file = open('11/input.txt', 'r')
    line = file.read()
    total = do_challenge_a(line)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")
    print(f'Total: {total}')


def do_challenge_a(line):
    blinks = 25
    numbers = []
    for number_str in line.split(' '):
        numbers.append(number_str)
    print(f'Found numbers {numbers}')
    skip_indexes = []
    current_blink = 0
    while current_blink != blinks:
        # print(f'Starting new blink')
        for n_index, number_str in enumerate(numbers):
            # print(f'Processing number {number_str}')
            if n_index in skip_indexes:
                # print(f'Skipping index {n_index}: {number_str}')
                continue
            if number_str == '0':
                numbers[n_index] = '1'
            elif len(number_str) % 2 == 0:
                middle_index = len(number_str) // 2
                first_half = number_str[:middle_index]
                second_half = number_str[middle_index:]
                if all(s == '0' for s in second_half):
                    second_half = '0'
                second_half = str(int(second_half))
                numbers[n_index] = str(int(first_half))
                numbers.insert(n_index + 1, second_half)
                skip_indexes.append(n_index + 1)
            else:
                new_number = int(number_str) * 2024
                # print(f'No rules, inserting {number_str} * 2024 = {new_number} at {n_index}')
                numbers[n_index] = str(new_number)
        skip_indexes = []
        current_blink += 1
        # print(f'Result after blink {numbers}')

    return len(numbers)

