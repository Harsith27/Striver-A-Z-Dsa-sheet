def fibonacci(n):
    if n<=2:
        return n-1
    return fibonacci(n-1)+fibonacci(n-2)
n=int(input())
for i in range(1,n+1):
    print(fibonacci(i),end=" ")
