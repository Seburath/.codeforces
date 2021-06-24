def count_divs(a, b):
    divs = 0
    while a != 0:
        a = a // b
        divs += 1

    return divs


def solve(ab):
    a, b = map(int, ab.split())
    first_move = 1 if b == 1 else 0
    b += 1 if b == 1 else 0

    divs = count_divs(a, b)
    b_moves = 0

    for i in range(divs):
        test_divs = count_divs(a, b+i)
        if test_divs < divs - i:
            divs = test_divs 
            b_moves = i

    return divs + b_moves + first_move


if __name__ == '__main__':
    tests = []
    for test in range(int(input())):
        tests.append(input())
    
    for test in tests:
        print(solve(test))


def test():
    assert solve('9 2') == 4
    assert solve('1337 1') == 9
    assert solve('1 1') == 2
    assert solve('1 2') == 1
    assert solve('2 1') == 3
    assert solve('2 2') == 2
    assert solve('10 1') == 5
