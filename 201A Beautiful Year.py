def solve(year):
    year = int(year)
    beautiful_year = False
    counter = 0
    while beautiful_year == False:
        counter += 1
        next_year = list(str(year + counter))
        while next_year:
            beautiful_year = True
            if next_year.pop() in next_year:
                beautiful_year = False 
                break

    return year + counter


if __name__ == '__main__':
    print(solve(input())) 


def test():
    assert solve('1993') == 2013
    assert solve('2013') == 2014
