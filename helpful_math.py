s = input().split("+")

s.sort()

r = ""
for i in s:
    r += i + '+'

print(r[:-1])
