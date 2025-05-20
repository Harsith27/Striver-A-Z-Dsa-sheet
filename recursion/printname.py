def printName(n):
    if n==0:
        return
    print("Harsith")
    printName(n-1)
n=int(input())
printName(n)