#!/bin/python3

import sys
from collections import Counter


def isValid(s):
    c = Counter(s)
    flag = 0
    mc = c.most_common(1)[0][1]
    mc2 = mc
    if len(c) > 1:
        mc2 = c.most_common(2)[1][1]
    if mc - mc2 > 1:
        return 'NO'
    if mc - mc2 == 1:
        mc = mc2
    for e in c:
        if c[e] != mc:
            flag += 1
    if flag > 1:
        return 'NO'
    else:
        return 'YES'


s = input().strip()
result = isValid(s)
print(result)
