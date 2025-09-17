# def frogjumpk(n,k,nums,memo={}):
#     if n==0:
#         return 0
#     if n in memo:
#         return memo[n]
#     min_cost=float('inf')
#     for i in range(1,k+1):
#         if n-i>=0:
#             cost=frogjumpk(n-i,k,nums,memo)+abs(nums[n]-nums[n-i])
#             min_cost=min(min_cost,cost)
#     memo[n]=min_cost
#     return min_cost
# nums=list(map(int,input().split()))
# k=int(input())
# print(frogjumpk(len(nums)-1,k,nums))


#brute force
def frogjumpk(n,k,nums):
    if n==0:
        return 0
    min_cost=float('inf')
    for i in range(1,k+1):
        if n-i>=0:
            cost=frogjumpk(n-i,k,nums)+abs(nums[n]-nums[n-i])
            min_cost=min(min_cost,cost)
    return min_cost
nums=list(map(int,input().split()))
k=int(input())
print(frogjumpk(len(nums)-1,k,nums))