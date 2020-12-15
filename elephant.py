def solve(x):
    steps = 0
    mod = x
    for i in range(5,1,-1):
        steps +=  mod // i
        mod %= i

    return steps


if __name__ == "__main__":
    x = int(input())
    print(solve(x))


def test():
    assert solve(5) == 1
    assert solve(12) == 3
