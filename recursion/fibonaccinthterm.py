def fibonacci(n):
    if n<2:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
n=int(input())
print(fibonacci(n-1))

# check whether the fibonacci is 1  based or 2 based and make changes accordingly 
