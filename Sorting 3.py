n=input()
arr=list(map(int,input().split()))
e=arr[-1]
for i in range(len(arr)-1):
    i+=1
    i*=-1
    if e<arr[i-1]:
        arr[i]=arr[i-1]
        print(*arr)
        if i - 1 == -len(arr):
            arr[0] = e
            print(*arr)
            break
    else:
        arr[i]=e
        print(*arr)
        break