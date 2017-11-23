#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
d1,d2=0,0
for i in range(len(a)):
    d1+=a[i][i]
    d2+=a[i][-i-1]
print (abs(d1-d2))