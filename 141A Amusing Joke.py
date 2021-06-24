def solve(w1, w2, w3):
    w =  list(w1 + w2)
    w3 = list(w3)
    for i in w:
        if i in w3:
            w3.pop(w3.index(i))
        else:
            return 'NO'

    if len(w3) == 0:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':

    print(solve(input(), input(), input()))


def test():
    assert solve('SANTACLAUS', 'DEDMOROZ', 'SANTAMOROZDEDCLAUS') == 'YES'
    assert solve('PAPAINOEL', 'JOULUPUKKI', 'JOULNAPAOILELUPUKKI') == 'NO'
    assert solve('BABBONATALE', 'FATHERCHRISTMAS', 'BABCHRISTMASBONATALLEFATHER') == 'NO'
