#!/bin/python3

import sys
from collections import Counter


def gameOfThrones(s):
    c = Counter(s)
    d = dict(c)
    vals = d.values()  # all counts collected
    odd = 0  # sufficient condition is to have at most 1 odd letter
    for e in vals:
        if e % 2 != 0:
            odd += 1
    if odd <= 1:
        return 'YES'
    return 'NO'


s = input().strip()
result = gameOfThrones(s)
print(result)