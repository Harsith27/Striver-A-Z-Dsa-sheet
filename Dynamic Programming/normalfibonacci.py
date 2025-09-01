def fibonacci(n):
    if n<2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
n=int(input())
for i in range(n):
    print(fibonacci(i),end=" ")