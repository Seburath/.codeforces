

def solve(w1, w2):
    return 'YES' if ''.join(reversed(list(w1))) == w2 else 'NO'


if __name__ == '__main__':
    print(solve(input(), input()))


def test():
    assert solve('code', 'edoc') == 'YES'
    assert solve('ada', 'aba') == 'NO'
    assert solve('code', 'code') == 'NO'
