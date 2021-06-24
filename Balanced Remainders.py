from math import log


def solve(a):
    a = list(map(int, a.split()))
    c = [len([i for i in a if i % 3 == divisor]) for divisor in range(3)]
    cmax = len(a)/3

    moves = 0
    for i in range(3):
        c[i] += c[i-1] - cmax if c[i-1] > cmax else 0
        moves += c[i] - cmax if c[i] > cmax else 0

    return int(moves)


if __name__ == '__main__':
    t = int(input())
    tests = []

    for i in range(t):
        test_len = input()
        tests.append(input())

    for i in tests:
        print(solve(i))


def test():
    assert solve('0 2 5 5 4 8') == 3
    assert solve('7 1 3 4 2 10 3 9 6') == 3
