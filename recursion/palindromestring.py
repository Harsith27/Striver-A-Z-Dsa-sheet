def palindrome(rev,i,j):
    if i>=j:
        return True
    if rev[i]!=rev[j]:
        return False
    return palindrome(rev,i+1,j-1)

s=input()
print(palindrome(s,0,len(s)-1))

#dont use rev=s for creating a copy of s, use rev=s[:] or rev=list(s) or rev=s.copy()

#if Capital letters are treated equal as their small letter equivalents, then use s=s.lower() before calling the function
