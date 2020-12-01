
def solve():
    n = int(input())

    x = 0
    for i in range(n):
        operation = input()
        if '+' in operation:
            x += 1
        if '-' in operation:
            x -= 1

    print(x)


if __name__ == __name__:
    solve()
