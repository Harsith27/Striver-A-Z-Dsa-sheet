def checkprime(n):
    if(n==0 or n==1):
        return "This is neither prime nor composite"
    for i in range(2,n):
        if (n%i==0):
            return False
    return True

n=int(input())
print(checkprime(n))