n=int(input())
ar=input().split()
ar=list(map(int,ar))
left=[]
right=[]
p=ar[0]
for e in ar[1:]:
    if e < p:
        left.append(e)
        ar.remove(e)
    elif e > p:
        right.append(e)
        ar.remove(e)
print(*left,*ar,*right)