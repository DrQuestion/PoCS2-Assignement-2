#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
a,b,c=0,0,0
for e in arr:
    if e > 0:
        a+=1
    elif e < 0:
        b+=1
    else:
        c+=1
print (a/n)
print (b/n)
print (c/n)