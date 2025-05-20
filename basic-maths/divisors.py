def divisor(n):
    div=[]
    for i in range(1,n+1):
        if(n%i==0):
            div.append(i)
    return  div
n=int(input())
print(*(sorted(divisor(n))))

