# def bestSum(targetSum,nums,memo={}):
#     if targetSum==0:
#         return []
#     if targetSum<0:
#         return None
#     if targetSum in memo:
#         return memo[targetSum]
#     smallestarr=None
#     for num in nums:
#         remainder=targetSum-num
#         remainderval=bestSum(remainder,nums)
#         if remainderval!=None:
#             arr=remainderval+[num]
#             if (smallestarr==None) or (len(arr)<len(smallestarr)):
#                 smallestarr=arr
#     memo[targetSum]=smallestarr
#     return memo[targetSum]

# targetSum=int(input())
# nums=list(map(int,input().split()))
# print(bestSum(targetSum,nums))



# def howSum(targetSum,nums,memo={}):
#     if targetSum==0:
#         return []
#     if targetSum<1:
#         return None
#     if targetSum in memo:
#         return memo[targetSum]
#     for num in nums:
#         remainder=targetSum-num
#         remainderval=howSum(remainder,nums,memo)
#         if remainderval!=None:
#             memo[targetSum] = remainderval+[num]
#             return memo[targetSum]
#     memo[targetSum]=None
#     return None

# targetSum=int(input())
# nums=list(map(int,input().split()))
# print(howSum(targetSum,nums))