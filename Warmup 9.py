#!/bin/python3
from collections import Counter
import sys

def birthdayCakeCandles(n, ar):
    d=Counter(ar)
    return d.most_common(1)[0][1]

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)