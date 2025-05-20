from math import *
def armstrong(n):
    temp=n
    sum=0
    k=int(log10(n))+1
    while(temp>0):
        p=temp%10
        sum=sum+p**k
        temp=temp//10
    return sum==n

n=int(input())
print(armstrong(n))


