n = int(input())
stones = input()

count = 0
last_stone = ""
for stone in stones:
    if stone != last_stone:
        last_stone = stone
    else:
        count += 1

print(count)
