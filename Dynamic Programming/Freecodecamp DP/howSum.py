def howSum(targetSum,nums):
    if targetSum==0:
        return []
    if targetSum<0:
        return None
    for num in nums:
        remainder=targetSum-num
        remainderResult=howSum(remainder,nums)
        if remainderResult!=None:
            return remainderResult+[num]
    return None

targetSum=int(input())
nums=list(map(int,input().split()))
print(howSum(targetSum,nums))