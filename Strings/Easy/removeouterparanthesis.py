def removeouterparanthesis(s):
    count=0
    res=""
    for i in range(len(s)):
        if s[i] =="(":
            if count>0:
                res+=s[i]
            count+=1
        else:
            count-=1
            if count>0:
                res+=s[i]
    return res

s=input()
print(removeouterparanthesis(s))