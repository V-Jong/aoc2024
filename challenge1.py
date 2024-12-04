def do_challenge():
    file = open('1/input.txt', 'r')
    lines = file.readlines()
    total = do_challenge_b(lines)
    print(f'Total: {total}')


def do_challenge_a(lines):
    total = 0
    sizes_left = []
    sizes_right = []
    for line in lines:
        line = line.replace('\n', '')
        sizes_split = line.split('   ')
        sizes_left.append(sizes_split[0])
        sizes_right.append(sizes_split[1])
    sizes_left.sort()
    sizes_right.sort()
    for index, l_value in enumerate(sizes_left):
        r_value = sizes_right[index]
        abs_diff = abs(int(l_value) - int(r_value))
        # print(f'Asbolute diff between {l_value} and {r_value} = {abs_diff}')
        total = total + abs_diff
    return total


def do_challenge_b(lines):
    total = 0
    sizes_left = []
    sizes_right = []
    for line in lines:
        line = line.replace('\n', '')
        sizes_split = line.split('   ')
        sizes_left.append(int(sizes_split[0]))
        sizes_right.append(int(sizes_split[1]))
    for index, l_value in enumerate(sizes_left):
        occurrence_count = sizes_right.count(l_value)
        similarity = l_value * occurrence_count
        total = total + similarity
    return total
