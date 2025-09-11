def bestSum(targetSum,nums):
    if targetSum==0:
        return []
    if targetSum<0:
        return None
    smallestarr=None
    for num in nums:
        remainder=targetSum-num
        remaindervalue=bestSum(remainder,nums)
        if remaindervalue!=None:
            arr=remaindervalue+[num]
            if (smallestarr==None or (len(arr)<len(smallestarr))):
                smallestarr=arr
    return smallestarr

targetSum=int(input())
nums=list(map(int,input().split()))
print(bestSum(targetSum,nums))