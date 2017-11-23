#!/bin/python3

import sys

def timeConversion(s):
    if s[-2:]=='AM':
        if s[:2]=='12':
            S='00'+s[2:-2]
        else:
            S=s[:-2]
    else:
        if s[:2]=='12':
            S=s[:-2]
        else:
            S=str(int(s[:2])+12)+s[2:-2]
    return S

s = input().strip()
result = timeConversion(s)
print(result)
