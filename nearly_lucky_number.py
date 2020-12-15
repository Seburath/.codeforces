

def solve(num):
    counter = 0
    for digit in num:
        if digit == '4' or digit == '7':
            counter += 1

    for digit in str(counter):
        if digit != '4' and digit != '7':
            return 'NO'
    return 'YES'

if __name__ == '__main__':
    print(solve(input()))


def test():
    assert solve('40047') == 'NO'
    assert solve('7747774') == 'YES'
    assert solve('1000000000000000000') == 'NO'
