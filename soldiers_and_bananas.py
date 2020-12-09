k, n, w = map(int, input().split())

r = int(w/2 * (1+w) * k - n)

print(r) if int(r) >= 0 else print(0)
