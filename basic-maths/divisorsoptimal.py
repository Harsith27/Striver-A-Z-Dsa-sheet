from math import isqrt
def divisor(n):
    div=[]
    for i in range(1,isqrt(n)+1):
        if(n%i==0):
            div.append(i)
            if (i!=n//i):
                div.append(n//i)
    return  div

n=int(input())
print(*(sorted(divisor(n))))

