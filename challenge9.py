import time


def do_challenge():
    start_time = time.time()
    file = open('9/input.txt', 'r')
    line = file.read()
    total = do_challenge_a(line)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")
    print(f'Total: {total}')


def do_challenge_a(line):
    total = 0
    blocks = []
    id_number = 0
    for c_index, c in enumerate(line):
        block_times = int(c)
        if c_index % 2 == 0:
            id_str = str(id_number)
            count_append = 0
            # for id_char in id_str:
            #     while count_append < block_times:
            #         blocks.append(id_char)
            #         count_append += 1
            while count_append < block_times:
                blocks.append(id_str)
                count_append += 1
            id_number += 1
        else:
            blocks.extend(['.'] * block_times)
    # print(f'blocks ({len(blocks)}) {blocks}')

    count_dots_total = len([block for block in blocks if block == '.'])
    dots_from_end = count_dots_from_end(blocks)
    # print(f'number of dots: {count_dots_total}')
    # print(f'dots from end: {dots_from_end}')
    # print(f'dots from end: {find_next_number_from_end(blocks)}')
    while dots_from_end != count_dots_total:
        next_dot_index = find_next_dot(blocks)
        digit_to_insert_index = find_next_number_from_end(blocks)
        digit_to_insert = blocks[digit_to_insert_index]

        blocks[next_dot_index] = digit_to_insert
        blocks[digit_to_insert_index] = '.'
        dots_from_end = count_dots_from_end(blocks)

    for b_index, b in enumerate(blocks):
        if b.isdigit():
            total += b_index * int(b)
    return total


def count_dots_from_end(lst):
    count = 0
    for item in reversed(lst):
        if item == ".":
            count += 1
        else:
            break
    return count


def find_next_number_from_end(lst):
    for i, item in enumerate(reversed(lst)):
        if item.isdigit():
            return len(lst) - 1 - i


def find_next_dot(lst):
    for i, item in enumerate(lst):
        if item == '.':
            return i
