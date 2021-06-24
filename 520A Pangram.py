def solve(word):
    word = set(word.lower())
    return 'YES' if len(word) == 26 else 'NO'


if __name__ == '__main__':
    n = input()
    print(solve(input()))


def test():
    assert solve('toosmallword') == 'NO'
    assert solve('TheQuickBrownFoxJumpsOverTheLazyDog') == 'YES'
