import time


def do_challenge():
    start_time = time.time()
    file = open('10/test.txt', 'r')
    lines = file.readlines()
    total = do_challenge_a(lines)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")
    print(f'Total: {total}')


def do_challenge_a(lines):
    total = 0
    # Do solution
    return total

