t = int(input())

problems = 0
for i in range(t):
    p = sum(map(int, input().split()))
    if p >= 2:
        problems += 1

print(problems)
