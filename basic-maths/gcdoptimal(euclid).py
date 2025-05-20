def euclidgcd(a,b):
    while(a>0 and b>0):
        if a>b:
            a=a%b
        else:
            b=b%a
    return a if a!=0 else b

a=int(input())
b=int(input())
print(euclidgcd(a,b))

# for the subration method(euclid gcd) just substitute % with -
