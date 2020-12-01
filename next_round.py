n, k = map(int, input().split())
a = list(map(int, input().split()))


if a[0] == 0:
    print(0)
else:
    lastone = a[k]

    if lastone == 0:
        added = a[:k].count(lastone) * -1
    else:
        for i, participant in enumerate(a[k -1 :]):
            added = i 
            if participant != lastone:
                break

    print(k + added - 1)
