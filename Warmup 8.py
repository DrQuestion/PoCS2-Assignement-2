#!/bin/python3

from itertools import combinations
import sys

arr = list(map(int, input().strip().split(' ')))
l=list(combinations(arr,4))
for i in range(len(l)):
    l[i]=sum(l[i])
print (min(l),max(l))