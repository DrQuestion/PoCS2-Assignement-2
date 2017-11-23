#!/bin/python3

import sys

def super_reduced_string(s):
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            s=s[:i]+s[i+2:]
            return super_reduced_string(s)
    if not s:
        return 'Empty String'
    return s
s = input().strip()
result = super_reduced_string(s)
print(result)
