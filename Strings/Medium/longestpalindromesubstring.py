def helper(res, reslen, s, l, r):
    while l>=0 and r<len(s) and s[l]==s[r]:
        if r-l+1>reslen:
            res=s[l:r+1]
            reslen=r-l+1
        l-=1
        r+=1
    return res,reslen
def longest_reslen_substring(s):
    res=""
    reslen=0
    for i in range(len(s)):
        res,reslen=helper(res,reslen,s,l=i, r=i)
        res,reslen=helper(res,reslen,s,l=i, r=i+1)
    return res

s=input()
