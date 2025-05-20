def seive(n):
    if n<2:
        return []
    isprime=[1] * n
    isprime[0],isprime[1]=0,0
    for i in range(2,int(n**0.5)+1):
        if isprime[i]:
            for j in range(i*i,n,i):
                isprime[j]=0
    return list(i for i in range(n) if isprime[i])

n=int(input())
print(*seive(n))

