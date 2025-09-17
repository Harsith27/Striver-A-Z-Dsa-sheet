def houserobber(n,nums,memo={}):
    if n==0:
        return nums[0]
    if n<0:
        return 0
    if n in memo:
        return memo[n]
    rob=nums[n]+houserobber(n-2,nums,memo)
    skip=houserobber(n-1,nums,memo)
    memo[n]=max(rob,skip)
    return memo[n]
nums=list(map(int,input().split()))
print(houserobber(len(nums)-1,nums))