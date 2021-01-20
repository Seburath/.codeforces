#NOT WORKING
def solve(n, x, y):
    x = set(map(int, x.split()))
    y = set(map(int, y.split()))
    levels = set.union(x, y)
    #return 'I become the guy.' if len(levels) == int(n) else 'Oh, my keyboard!'

    return ["Oh, my keyboard!","I become the guy."][int(n)==len(x.union(set(y)))]

if __name__ == '__main__':
    print(solve(input(), input(), input()))


def test():
    assert solve('4', '3 1 2 3', '2 2 4') == 'I become the guy.'
    assert solve('4', '3 1 2 3', '2 2 3') == 'Oh, my keyboard!'
