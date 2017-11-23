#!/bin/python3

import sys

n = int(input().strip())
s = input().strip()
k = int(input().strip())
lowalpha = 'abcdefghijklmnopqrstuvwxyz'
upalpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
newstring = []
for e in s:
    if e.isupper():
        l = upalpha.find(e)
        newstring.append(upalpha[l + k - 26 * ((k // 26) + 1)])
    elif e.islower():
        l = lowalpha.find(e)
        newstring.append(lowalpha[l + k - 26 * ((k // 26) + 1)])
    else:
        newstring.append(e)
print(''.join(newstring))
