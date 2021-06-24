def solve(p, moves):
    px, py = map(int, p.split())

    us = moves.count('U')
    ds = moves.count('D')
    rs = moves.count('R')
    ls = moves.count('L')

    if us >= py >= 0 or ds * -1 <= py <= 0:
        if rs >= px >= 0 or ls * -1 <= px <= 0:
            return 'YES'

    return 'NO'


if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        p = input()
        moves = input()
        print(solve(p, moves))


def test():
    assert solve('10 5', 'RRRRRRRRRRUUUUU') == 'YES'
    assert solve('1 1', 'UDDDRLLL') == 'YES'
    assert solve('3 -2', 'RDULRLLDR') == 'YES'
    assert solve('-1 6', 'RUDURUUUUR') == 'NO'
