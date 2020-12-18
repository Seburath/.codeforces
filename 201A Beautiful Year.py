def solve(year):
    year = int(year)
    i = 0

    is_beautiful = False
    while not is_beautiful:
        i += 1

        next_year = list(str(year + i))
        while next_year != []:
            if next_year.pop() in next_year:
                break
        else:
            is_beautiful = True

    return year + i


if __name__ == '__main__':
    print(solve(input())) 


def test():
    assert solve('1993') == 2013
    assert solve('2013') == 2014
