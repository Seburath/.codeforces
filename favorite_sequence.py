from collections import deque


def solve(case):
    sequence = deque(case.split())
    solved = []
    for i in range(len(sequence)):
        if i % 2 == 0:
            solved.append(sequence.popleft())
        else:
            solved.append(sequence.pop())
    
    str_solved = ' '
    return str_solved.join(solved)

if __name__ == '__main__':
    cases = int(input())
    solved_cases = []
    for case in range(cases):
        l = input()
        solved_cases.append(solve(input()))

    for sequence in solved_cases:
        print(sequence)


def test():
    assert solve('3 4 5 2 9 1 1') == '3 1 4 1 5 9 2'
    assert solve('9 2 7 1') == '9 1 2 7' 
    assert solve('8 4 3 1 2 7 8 7 9 4 2') == '8 2 4 4 3 9 1 7 2 8 7' 
