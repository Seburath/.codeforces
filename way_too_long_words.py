t = int(input())

w = []
for i in range(t):
    word = input()
    if len(word) <= 10:
        w.append(word)
    else:
        w.append(word[0] + str(len(word) - 2) + word[-1])

for i in w:
    print(i)
