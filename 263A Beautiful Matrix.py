def solve(matrix):
    for i, row in enumerate(matrix.split('\n')):
        if '1' in row:
            x_dist = abs(row.find('1')//2 - 2)
            y_dist = abs(i - 2)
            return x_dist + y_dist


if __name__ == '__main__':
    matrix = ''
    for i in range(5):
        matrix += input() + '\n'

    print(solve(matrix))


def test():
    assert solve("""0 0 0 0 0
0 0 0 0 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
""") == 3

    assert solve("""0 0 0 0 0
0 0 0 0 0
0 1 0 0 0
0 0 0 0 0
0 0 0 0 0
""") == 1
