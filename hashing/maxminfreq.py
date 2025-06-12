from collections import Counter
arr=list(map(int,input().split()))
mydict=Counter(arr)
maxv=float("-inf")
minv=float("inf")
maxele,minele=0,0
for k in mydict:
    if mydict[k]>maxv:
        maxv=mydict[k]
        maxele=k
    elif mydict[k]<minv:
        minv=mydict[k]
        minele=k
print(maxele,minele)
