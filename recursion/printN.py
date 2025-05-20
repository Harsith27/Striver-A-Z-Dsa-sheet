def printN(n,c=0):
    if n==c:
        return
    print(n)
    printN(n,c+1)

n=int(input())
print(printN(n))
