def solve(poly):
    data = {'T':4, 'C':6, 'O':8, 'D':12, 'I':20}

    faces = 0
    for i in poly.split('\n'):
        faces += data[i[0]]

    return faces


if __name__ == '__main__':
    n = int(input())
    poly = []

    for i in range(n):
        poly.append(input())

    print(solve('\n'.join(poly)))


def test():
    assert solve('''Icosahedron
Cube
Tetrahedron
Dodecahedron''') == 42
    assert solve('''Dodecahedron
Octahedron
Octahedron''') == 28
