def fibonacci(n):
    if n<=2:
        return n-1
    return fibonacci(n-1)+fibonacci(n-2)
n=int(input())
print(fibonacci(n))

# check whether the fibonacci is 1  based or 2 based and make changes accordingly 
#for 1 indexed based keep return n-1 and if n<=2 
#for 0 indexed based keep return n