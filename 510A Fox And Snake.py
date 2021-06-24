def solve(nm):
    n, m = map(int, nm.split())

    snake = []
    for i in range(n):
        if (i-1)%2 != 0:
            snake.append('#' * m)
        elif (i+1)%4 != 0:
            snake.append('.' * (m-1) + '#')
        else:
            snake.append('#' + '.' * (m-1))

    return '\n'.join(snake)


if __name__ == '__main__':
    print(solve(input()))


def test():
    assert solve('3 3') == '''###
..#
###'''
    assert solve('3 4') == '''####
...#
####'''
    assert solve('5 3') == '''###
..#
###
#..
###'''
