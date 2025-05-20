def gcd(a,b):
    g=1
    for i in range(min(a,b),0,-1):
        if a%i==0 and b%i==0:
            g=i
            break;
    return g
a=int(input())
b=int(input())
print(gcd(a,b))