def solve(letters):
    l = 'abcdefghijklmnopqrstuvwxyz'
    return len(set([a for a in letters if a in l]))


if __name__ == '__main__':
    print(solve(input()))


def test():
    assert solve('{a, b, c}') == 3
    assert solve('{b, a, b, a}') == 2
    assert solve('{}') ==  0
