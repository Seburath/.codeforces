def solve(num1, num2):
    numbers = zip(num1, num2)
    result = ['0' if bit1 == bit2 else '1' for bit1, bit2 in numbers]
    return ''.join(result)


if __name__ == '__main__':
    print(solve(input(), input()))


def test():
    assert solve('1010100','0100101') == '1110001'
    assert solve('000','111') == '111'
