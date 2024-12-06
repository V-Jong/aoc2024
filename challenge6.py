import threading
import time

directions = {
    'up': (0, -1),
    'down': (0, 1),
    'left': (-1, 0),
    'right': (1, 0)
}
block_directions = {
    'up': (1, -1),
    'down': (-1, 1),
    'left': (-1, -1),
    'right': (1, 1)
}
grid = {}
passed_nodes = {}


def do_challenge():
    file = open('6/test.txt', 'r')
    lines = file.read().splitlines()
    thread = threading.Thread(target=do_challenge_b(lines))
    thread.start()


def do_challenge_a(lines):
    start_time = time.time()
    max_x = 0
    max_y = len(lines)
    start_x = -1
    start_y = -1
    for l_index, line in enumerate(lines):
        if max_x == 0:
            max_x = len(line)
        for c_index, c in enumerate(line):
            # print(f'Adding char {c} to ({c_index},{l_index})')
            if c == '^':
                start_x = c_index
                start_y = l_index
                # print(f'Found start at: ({start_x}, {start_y})')
            grid.update({(c_index, l_index): c})

    open('6/debug.txt', 'w').close()
    count_traveled((start_x, start_y), 'up', max_x, max_y)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")
    print(f'Traveled: {get_travel_count()}')


def do_challenge_b(lines):
    start_time = time.time()
    max_x = 0
    max_y = len(lines)
    start_x = -1
    start_y = -1
    for l_index, line in enumerate(lines):
        if max_x == 0:
            max_x = len(line)
        for c_index, c in enumerate(line):
            # print(f'Adding char {c} to ({c_index},{l_index})')
            if c == '^':
                start_x = c_index
                start_y = l_index
                # print(f'Found start at: ({start_x}, {start_y})')
            grid.update({(c_index, l_index): c})

    open('6/debug.txt', 'w').close()
    obstacles = [key for key, value in grid.items() if value == '#']
    for obstacle in obstacles:
        print(f'Checking if can make closed loop with {obstacle}, {obstacle[0]} - {obstacle[1]}')
        left_obstacles = [(x, y) for (x, y) in obstacles if y == obstacle[1] - 1]
        right_obstacles = [(x, y) for (x, y) in obstacles if x == obstacle[0] - 1]
        if len(left_obstacles) == 1 and len(right_obstacles) == 1:
            left_obstacles = left_obstacles[0]
            right_obstacles = right_obstacles[0]
            proposed = (left_obstacles[0] - 1, right_obstacles[1] - 1)
            print(f'From obstacle {obstacle}, found left {left_obstacles}, right {right_obstacles} and proposing {proposed}')

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")
    print(f'Traveled: {get_travel_count()}')


def count_traveled(current_node: (int, int), direction: str, max_x: int, max_y: int):
    stack = [(current_node, direction, 0)]  # (node, direction, counter)

    with open("6/debug.txt", "a") as f:
        while stack:
            current_node, direction, counter = stack.pop()

            print(
                f'\nChecking {current_node} while going {direction}, current count {counter}',
                file=f)
            f.flush()
            if (current_node[0] < 0 or current_node[0] >= max_x) or (current_node[1] < 0 or current_node[1] >= max_y):
                print(f'Stopping since {current_node} in out of bounds, returning {counter}', file=f)
                f.flush()
                continue
            current_char = grid.get(current_node)
            print(f'Character at {current_node} is {current_char}', file=f)
            f.flush()

            if current_char == '.' or current_char == '^':
                if not any(pn for pn in passed_nodes if pn[0] == current_node[0] and pn[1] == current_node[1]):
                    print(f'Not encountered {current_node}, adding to cache', file=f)
                    passed_nodes.update({(current_node[0], current_node[1]): 1})
                    counter += 1
                next_direction = directions.get(direction)
                next_node = (current_node[0] + next_direction[0], current_node[1] + next_direction[1])
                print(f'Going {direction} to {next_node}', file=f)
                f.flush()
                stack.append((next_node, direction, counter))
            elif current_char == "#":
                new_direction = ''
                if direction == 'right':
                    new_direction = 'down'
                if direction == 'up':
                    new_direction = 'right'
                if direction == 'left':
                    new_direction = 'up'
                if direction == 'down':
                    new_direction = 'left'
                next_direction = block_directions.get(new_direction)
                next_node = (current_node[0] + next_direction[0], current_node[1] + next_direction[1])
                print(f'Going {new_direction} to {next_node}', file=f)
                f.flush()
                stack.append((next_node, new_direction, counter))


def get_travel_count():
    count_checks = 0
    for node in passed_nodes:
        count_checks += 1
    return count_checks
