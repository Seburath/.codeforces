def solve(p):
    p = list(map(int, p.split()))
    r = list(range(len(p)))
    for i, e in enumerate(p):
        r[e-1] = str(i+1)

    return ' '.join(r)


if __name__ == '__main__':
    n = input()
    print(solve(input()))


def test():
    assert solve('2 3 4 1') == '4 1 2 3'
    assert solve('1 3 2') == '1 3 2'
