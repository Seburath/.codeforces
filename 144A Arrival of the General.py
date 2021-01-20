def solve(a):
    a = list(map(int, a.split()))
    amax = a.index(max(a))
    a.reverse()
    amin = a.index(min(a))

    if (len(a) - amax - 1) < amin:
        return amax + amin - 1
    else:
        return amax + amin


if __name__ == '__main__':
    n = input()
    print(solve(input()))


def test():
    assert solve('33 44 11 22') == 2
    assert solve('10 10 58 31 63 40 76') == 10

