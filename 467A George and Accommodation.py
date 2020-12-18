#!/usr/bin/env python
# -*- coding: utf-8 -*-


def valid_room(people):
    p, q = map(int, people.split())
    return 1 if q - p >= 2 else 0


if __name__ == '__main__':
    rooms = range(int(input()))

    valid_rooms = 0 
    for room in rooms:
        valid_rooms += valid_room(input())

    print(valid_rooms)

def test():
    assert valid_room('1 1') == 0
    assert valid_room('1 2') == 0
    assert valid_room('1 3') == 1
    assert valid_room('1 10') == 1
