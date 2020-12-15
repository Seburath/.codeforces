

def solve(word):
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    lower_count = len([letter for letter in word if letter in lowercase])
    upper_count = len(word) - lower_count

    return word.lower() if lower_count >= upper_count else word.upper()


if __name__ == "__name__":
    print(solve(input()))


def test():
    assert solve('HoUse') == 'house'
    assert solve('ViP') == 'VIP'
    assert solve('maTRIx') == 'matrix'
