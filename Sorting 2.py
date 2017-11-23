V=input()
n=input()
ar=input().split()
counter=0
for e in ar:
    if e==V:
        break
    if e!=V:
        counter+=1
print(counter)