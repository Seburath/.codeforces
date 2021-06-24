def solve(nk, h):
    n, k = map(int, nk.split())
    h = list(map(int, h.split()))
    
    while k > 0:
        for i, rock in enumerate(h):
            print(i)
            if i == len(h) - 1:
                return -1
            if h[i + 1] > rock:
                k -= h[i + 1] - rock

    return i

        

def test():
    assert solve('4 3', '4 1 2 3') == 2
    assert solve('2 7', '1 8') == 1
