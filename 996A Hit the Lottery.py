def solve(n):
    denominations = [100, 20, 10, 5, 1]
    
    bills = 0
    for denomination in denominations:
        bills += n // denomination
        n = n % denomination

    return bills


if __name__ == '__main__':
    print(solve(int(input())))


def test():
    assert solve(125) == 3
    assert solve(43) == 5
    assert solve(1000000000) == 10000000
