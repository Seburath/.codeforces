

def solve(h, friends):
    road = 0
    for friend in friends.split():
        if int(friend) <= h:
            road += 1
        else:
            road += 2
    return road


if __name__ == '__main__':
    n, h = map(int, input().split())
    print(solve(h, input()))
    

def test():
    assert solve(7, '4 5 14') == 4
    assert solve(1, '1 1 1 1 1 1') == 6
    assert solve(5, '7 6 8 9 10 5') == 11
