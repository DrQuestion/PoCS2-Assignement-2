n=input()
list=list(map(int,input().split()))
for i in range(1, len(list)):
    for j in range(0, i):
        if (list[i] < list[j]):
            item = list.pop(i)
            list.insert(j, item)
    print(*list)