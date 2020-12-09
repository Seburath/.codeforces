l, b = map(int, input().split())

years = 0
while l <= b:
    years += 1
    l *= 3
    b *= 2

print(years)
