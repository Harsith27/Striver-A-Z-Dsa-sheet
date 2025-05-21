def factorial(n,fact=1):
    if n==1:
        return fact
    fact=fact*n
    return factorial(n-1,fact)

n=int(input())
print(factorial(n))