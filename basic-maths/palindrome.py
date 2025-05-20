def palindrome(n):
    temp=n
    rev=0
    while(temp>0):
       p= temp%10
       rev=rev*10+p
       temp=temp//10
    return rev==n
n=int(input())
print(palindrome(n))