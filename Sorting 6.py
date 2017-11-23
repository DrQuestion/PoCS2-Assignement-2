n=input()
l=list(map(int,input().split()))
counter=0
for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
            l[j+1] = l[j]
            j -= 1
            counter+=1
        l[j+1] = key

print (counter)