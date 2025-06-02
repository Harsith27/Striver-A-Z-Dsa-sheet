arr=list(map(int,input().split()))
queries=list(map(int,input().split()))
mydict={}
for num in arr:
    mydict[num]=mydict.get(num,0)+1
for q in queries:
    print(q,"->",mydict.get(q,0))


#approach 2
# arr=list(map(int,input().split()))
# queries=list(map(int,input().split()))
# mydict={}
# for num in arr:
#     if num in mydict:
#         mydict[num]+=1
#     else:
#         mydict[num]=1
# for q in queries:
#     print(q,"->",mydict[q] if q in mydict else 0)