def palindrome(temp,val):
    if temp==0:
        return val
    p=temp%10
    val=val*10 + p
    return palindrome(temp//10,val)

n=int(input())
print(palindrome(n,0)==n)
