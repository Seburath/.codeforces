trams = int(input())

min_capacity = 0
passengers = 0
for tram in range(trams):
    a, b =  map(int, input().split())
    passengers += b -a
    if passengers > min_capacity:
        min_capacity = passengers

print(min_capacity)
