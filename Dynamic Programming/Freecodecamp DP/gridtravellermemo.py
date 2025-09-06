def gridtraveller(m,n,memo={}):
    # look out for memo=None logic cuz this wont work for multiple input or multi cases 
    if n==0 or m==0:
        return 0
    if n==1 and m==1:
        return 1
    key=(max(m,n),min(m,n))
    if key in memo:
        return memo[key]
    memo[key]=gridtraveller(m-1,n,memo)+gridtraveller(m,n-1,memo)
    return memo[key]


# recursion brute force 
# def gridtraveller(m,n):
#     if n==0 or m==0:
#         return 0
#     if n==1 and m==1:
#         return 1
#     return gridtraveller(m-1,n)+gridtraveller(m,n-1)

n,m=map(int,input().split())
print(gridtraveller(m,n))