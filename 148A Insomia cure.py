def solve(k, l, m, n, d):
    if 1 in [k, l, m, n]:
        return d
    
    def is_hurt(dragon):
        return 0 in [dragon%k, dragon%l, dragon%m, dragon%n]

    dragons = list(range(1, d+1))
    return len([dragon for dragon in dragons if is_hurt(dragon)])


if __name__ == '__main__':
    def inp():
        return int(input())

    print(solve(inp(), inp(), inp(), inp(), inp()))


def test():
    assert solve(1,2,3,4,12) == 12
    assert solve(2,3,4,5,24) == 17
