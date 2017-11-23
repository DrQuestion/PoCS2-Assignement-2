d=dict()
for e in range(100):
    d[e]=0

n=int(input())
ar=input().split()
ar=list(map(int,ar))
for e in ar:
    d[e]+=1

print (*d.values())