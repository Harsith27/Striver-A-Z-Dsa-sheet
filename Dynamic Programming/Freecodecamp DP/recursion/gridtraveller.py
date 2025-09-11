#recursion brute force 
def gridtraveller(m,n):
    if n==0 or m==0:
        return 0
    if n==1 and m==1:
        return 1
    return gridtraveller(m-1,n)+gridtraveller(m,n-1)

n,m=map(int,input().split())
print(gridtraveller(m,n))