def gcd(a,b):
    g=1
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            g=i
    return g
a=int(input())
b=int(input())
print(gcd(a,b))
