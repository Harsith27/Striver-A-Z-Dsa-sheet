def isomorphic(s,t):
    mydict={}
    for i,j in zip(s,t):
        if i in mydict:
            if mydict[i]!=j:
                return False
        else:
            mydict[i]=j
    return len(set(mydict.values()))==len(mydict)     ### for the case of s=badc and t=bada where a and c map to the same value a which contradicts the stmt
s=input()
t=input()
print(isomorphic(s,t))