#!/bin/python3

import sys

s = input().strip()
count=1
for letter in s:
    if letter.isupper():
        count+=1
print(count)