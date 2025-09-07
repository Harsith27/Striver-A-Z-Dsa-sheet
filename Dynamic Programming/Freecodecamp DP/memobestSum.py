def bestSum(targetSum,nums,memo={}):
    if targetSum==0:
        return []
    if targetSum<0:
        return None
    if targetSum in memo:
        return memo[targetSum]
    smallestarr=None
    for num in nums:
        remainder=targetSum-num
        remaindervalue=bestSum(remainder,nums)
        if remaindervalue!=None:
            arr=remaindervalue+[num]
            if (smallestarr==None or (len(arr)<len(smallestarr))):
                smallestarr=arr
    memo[targetSum]=smallestarr
    return memo[targetSum]

targetSum=int(input())
nums=list(map(int,input().split()))
print(bestSum(targetSum,nums))