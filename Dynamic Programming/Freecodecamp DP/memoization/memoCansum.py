def Cansum(targetSum,nums,memo={}):
    if targetSum==0:
        return True
    if targetSum<0:
        return False
    if targetSum in memo:
        return memo[targetSum]
    for num in nums:
        if Cansum(targetSum-num,nums,memo)==True:
            memo[targetSum]=True
            return True
    memo[targetSum]=False
    return False

targetSum=int(input())
nums=list(map(int,input().split()))
print(Cansum(targetSum,nums))