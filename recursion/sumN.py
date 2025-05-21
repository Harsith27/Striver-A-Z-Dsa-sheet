def sumN(n,sum=0):
    if n==0:
        return sum 
    sum=sum+n
    return sumN(n-1,sum)

n=int(input())
print(sumN(n))


# when to write return statement for recursive case