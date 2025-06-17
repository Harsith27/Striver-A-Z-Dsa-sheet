def isomorphic(s,t):
    mydict={}
    for i,j in zip(s,t):
        if i in mydict:
            if mydict[i]!=j:
                return False
        else:
            mydict[i]=j
    return len(set(mydict.values()))==len(mydict)

s=input()
t=input()
print(isomorphic(s,t))