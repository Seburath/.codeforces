def solve(magnets):
    groups = -1
    last_magnet = ''
    for magnet in magnets.split('\n'):
        if magnet != last_magnet:
            groups += 1
        last_magnet = magnet

    return groups


if __name__ == '__main__':
    magnets = ''
    for i in range(int(input())):
        magnets += input() + '\n'

    print(solve(magnets))
        

def test():
    assert solve('''10
10
10
01
10
10
''') == 3
    assert solve('''01
01
10
10
''') == 2

