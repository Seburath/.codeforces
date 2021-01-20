def solve(layers):
    feeling = 'I hate '
    for i in range(layers-1):
        if i%2 == 0:
            feeling += 'that I love '
        else:
            feeling += 'that I hate '
        
    return feeling + 'it'


if __name__ == '__main__':
    layers = int(input())
    print(solve(layers))


def tests():
    assert solve(1) == 'I hate it'
    assert solve(3) == 'I hate that I love that I hate it'

