for i in range(5):
    row = input()
    if '1' in row:
        steps = abs(i - 2)+abs(row.find('1')/2 - 2)

print(int(steps))
