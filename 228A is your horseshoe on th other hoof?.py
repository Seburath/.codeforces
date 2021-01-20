def solve(shoes):
    shoes = list(map(int, shoes.split()))
    for shoe in set(shoes):
        shoes.remove(shoe)

    return len(shoes)


if __name__ == '__main__':
    print(solve(input()))


def test():
    assert solve('1 7 3 3') == 1
    assert solve('7 7 7 7') == 3
    assert solve('1 7 7 7') == 2
    assert solve('1 7 3 5') == 0
    assert solve('7 7 3 3') == 2
