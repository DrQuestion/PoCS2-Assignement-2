d=dict()
l=range(100)
l2=list()
n=int(input())

for i in range(n):  #preparing a dictionary where keys are the quantity relative to the input strings, and the values are lists containing all the elements having that quantity associated
    inp=input().split()
    s=str(i)+' '+inp[1] #strings are 'labelled' with their order of appearance: will need this label at the end
    k=int(inp[0])
    if k not in d:
        d[k]=[]
    d[k].append(s)  #good point of using lists is that they preserve the order of the elements being appended

for i in l: #used the 'helper list' to order the lists in d by keys, then concatenating them: at the end of the loop the elements are all together in the order they have to be
    if i in d:
        l2+=d[i]

for i,v in enumerate(l2):  #here comes how 'the twist' is solved: used the labels to determine which is the first half of inputs
    a=v.split()
    a[0]=int(a[0])
    if a[0] < n/2:
        l2[i]='-'
    else:
        l2[i]=a[1]

print (*l2)