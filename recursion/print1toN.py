def print1toN(n,t=1):
    if t>n:
        return
    print(t)
    print1toN(n,t+1)

n=int(input())
print1toN(n)