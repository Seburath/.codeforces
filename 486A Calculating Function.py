def solve(n):
    return n // 2 if n % 2 == 0 else (n + 1)  // -2


if __name__ == '__main__':
    print(solve(int(input())))


def tests():
    assert solve(4) == 2
    assert solve(5) == -3
