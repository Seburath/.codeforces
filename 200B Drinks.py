def solve(p):
    drinks = list(map(int, p.split()))
    return sum(drinks)/len(drinks)

if __name__ == '__main__':
    n = input()
    print(solve(input()))


def test():
    assert int(solve('50 50 100')) == int(66.666666666667)
    assert int(solve('0 25 50 75')) == int(37.500000000000)
