#!/bin/python3

import sys

def solve(a0, a1, a2, b0, b1, b2):
    alice=0
    bob=0
    for i in range(3):
        if(a0,a1,a2)[i]>(b0,b1,b2)[i]:
            alice+=1
        if(a0,a1,a2)[i]<(b0,b1,b2)[i]:
            bob+=1
    return alice,bob

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))


