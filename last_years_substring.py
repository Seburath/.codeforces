

def solve(case):
    if case == '2020': 
        return 'YES'

    s2020 = case.split('2020')
    if len(s2020) == 2:
        return 'YES' if s2020[0] == '' or s2020[1] == '' else 'NO'

    s202 = case.split('202')
    if len(s202) == 2:
        return 'YES' if s202[0][0] == '2' and s202[1] == '' else 'NO'

    s020 = case.split('020')
    if len(s020) == 2:
        return 'YES' if s020[0][0] == '2' and s020[1] == '' else 'NO'

    s20 = case.split('20')
    if len(s20) == 3:
        return 'YES' if s20[0] == '' and s20[2] == '' else 'NO'

    return 'NO'
        

if __name__ == '__main__':
    t = range(int(input()))
    solved_cases = []
    for case in t:
        l = input()
        solved_cases.append(solve(input()))

    for case in solved_cases:
        print(case)


def test():
    assert solve('20192020') == 'YES'
    assert solve('22019020') == 'YES'
    assert solve('2020') == 'YES'
    assert solve('20002') == 'NO'
    assert solve('729040') == 'NO'
    assert solve('200200') == 'NO'
