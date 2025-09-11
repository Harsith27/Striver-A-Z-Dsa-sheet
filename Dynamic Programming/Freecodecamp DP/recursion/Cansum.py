def Cansum(targetSum,nums):
    if targetSum==0:
        return True
    if targetSum<0:
        return False
    for num in nums:
        if Cansum(targetSum-num,nums)==True:
            return True
    return False

targetSum=int(input())
nums=list(map(int,input().split()))
print(Cansum(targetSum,nums))