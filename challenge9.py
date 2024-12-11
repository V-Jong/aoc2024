import time


def do_challenge():
    start_time = time.time()
    file = open('9/input.txt', 'r')
    line = file.read()
    total = do_challenge_b(line)
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


def do_challenge_b(line):
    total = 0
    blocks = []
    id_number = 0
    id_number_occurrence_map = dict()
    id_number_start_indexes_map = dict()
    for c_index, c in enumerate(line):
        block_times = int(c)
        if c_index % 2 == 0:
            id_str = str(id_number)
            count_append = 0
            id_number_start_indexes_map.update({id_number: [len(blocks) - 1]})
            while count_append < block_times:
                if count_append == 0:
                    current_id_index_list = []
                else:
                    current_id_index_list = id_number_start_indexes_map.get(id_number)
                blocks.append(id_str)
                last_element = len(blocks) - 1
                if len(current_id_index_list) > 0:
                    last_element = current_id_index_list[len(current_id_index_list) - 1] + 1
                current_id_index_list.append(last_element)
                id_number_start_indexes_map.update({id_number: current_id_index_list})
                count_append += 1
            id_number_occurrence_map.update({id_number: count_append})

            id_number += 1
        else:
            blocks.extend(['.'] * block_times)
    # print(f'blocks ({len(blocks)}) {blocks}')
    # print(f'id occurrences {id_number_occurrence_map}')
    # print(f'id indexes {id_number_start_indexes_map}')
    # print()

    id_number -= 1
    while id_number != 1:
        print(f'Checking ID: {id_number}')
        dot_index_search = 0
        next_dot_indexes_after = find_next_dots_after_index(blocks, dot_index_search, id_number_start_indexes_map.get(id_number)[0])
        while len(next_dot_indexes_after) != 0:
            to_fill = id_number_start_indexes_map.get(id_number)
            # print(f'Next first dots = {next_dot_indexes_after}')
            # print(f'To fill = {to_fill}')
            if len(next_dot_indexes_after) >= len(to_fill):
                for tf_index, to_fill_digit_index in enumerate(to_fill):
                    blocks[next_dot_indexes_after[tf_index]] = str(id_number)
                    blocks[to_fill_digit_index] = '.'
                next_dot_indexes_after = []
            else:
                dot_index_search = next_dot_indexes_after[-1]
                # print(f'No fit for {id_number} at {next_dot_indexes_after}, check for dots after {dot_index_search}')
                next_dot_indexes_after = find_next_dots_after_index(blocks, dot_index_search, to_fill[0])

        id_number -= 1
        print(f'Done ID: {id_number}')
        print()

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


def find_next_dots_after_index(lst, index_after, index_before):
    # print(f'Search for dots after {index_after} and before {index_before}')
    indexes = []
    first_dot_found = False
    for i, item in enumerate(lst):
        if item == '.' and index_after < i < index_before:
            if not first_dot_found:
                first_dot_found = True
            indexes.append(i)
            continue
        if item.isdigit() and not first_dot_found:
            continue
        if item.isdigit and first_dot_found:
            break
    # print(f'Found dots {indexes}')

    return indexes
