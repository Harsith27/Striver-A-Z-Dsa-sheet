def howSum(targetSum,nums,memo={}):
    if targetSum==0:
        return []
    if targetSum<0:
        return None
    if targetSum in memo:
        return memo[targetSum]
    for num in nums:
        remainder=targetSum-num
        remainderResult=howSum(remainder,nums)
        if remainderResult!=None:
            memo[targetSum] = remainderResult+[num]
            return memo[targetSum]
    memo[targetSum]=None
    return None 

targetSum=int(input())
nums=list(map(int,input().split()))
print(howSum(targetSum,nums))