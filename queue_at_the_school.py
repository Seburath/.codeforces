

def solve(queue_str, time):
    queue = list(queue_str)
    for t in range(time):
        for i in range(len(queue)-1, 0, -1):
            if queue[i] == 'G' and queue[i-1] == 'B':
                queue[i], queue[i-1] = 'B', 'G'

    return ''.join(queue)


if __name__ == '__main__':
    n, t = map(int, input().split())
    print(solve(input(), t))


def test():
    assert solve('BGGBG', 1) == 'GBGGB'
    assert solve('BGGBG', 2) == 'GGBGB'
    assert solve('GGGB', 1) == 'GGGB'
    assert solve('GGGBBB', 1) == 'GGGBBB'
    assert solve('BGGBBB', 2) == 'GGBBBB'
    assert solve('BGGGGG', 8) == 'GGGGGB'
    assert solve('BGGGGG', 4) == 'GGGGBG'
    assert solve('B', 4) == 'B'
    assert solve('G', 4) == 'G'
    assert solve('GB', 4) == 'GB'
    assert solve('BG', 4) == 'GB'
    assert solve('BG', 0) == 'BG'
