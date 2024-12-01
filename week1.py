import re


def do_challenge():
    file = open('1/input.txt', 'r')
    lines = file.readlines()
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
        total = total + abs_diff
        # print(f'Asbolute diff between {l_value} and {r_value} = {abs_diff}')
    print(f'Total: {total}')
