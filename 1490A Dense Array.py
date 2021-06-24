############ ---- Codeforces Template ---- ############
from sys import stdin.readline


input = stdin.readline

def intput():
    return(int(input()))

def mapint():
    return(list(map(int,input().split())))

def mapstr():
    return(list(map(int,input().split())))

def instr():
    s = input()
    return(list(s[:len(s) - 1]))

class Solver:
    def __init__(self, t):
        self.t = t
        self.tests = []

    def read():
        pass

    def read_mapint_skiping(self, skip):
        for line in range(0, self.t):
            skiping = [input() for j in range(skip)]
            self.tests.append(mapint())

        return self


    def run(self, solve):
        for test in self.tests:
            print(solve(test))
##################################################


def solve(a):
    counter = 0
    for i, e in enumerate(a):
        if i == len(a) - 1:
            continue

        amin = min(a[i], a[i+1])
        amax = max(a[i], a[i+1])
        extra_num = amin

        while amax/2 > extra_num:
            counter += 1
            extra_num *= 2

    return int(counter)


if __name__ == '__main__':
    n = intput()
    tests = Solver(n).read_mapint_skiping(1)
    tests.run(solve)


def test():
    assert Solve('''6
4
4 2 10 1
2
1 3
2
6 1
3
1 4 2
5
1 2 3 4 3
12
4 31 25 50 30 20 34 46 42 16 15 16
''') == '''5
1
2
1
0
3
'''
