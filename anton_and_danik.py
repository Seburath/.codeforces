

def solve(games):
    A_count = games.count('A')
    D_count = len(games) - A_count
    if A_count > D_count:
        return 'Anton'
    elif A_count < D_count:
        return 'Danik'
    else:
        return 'Friendship'


if __name__ == '__main__':
    l = input()
    print(solve(input()))


def test():
    assert solve('ADAAAA') == 'Anton'
    assert solve('DDDAADA') == 'Danik'
    assert solve('DADADA') == 'Friendship'
