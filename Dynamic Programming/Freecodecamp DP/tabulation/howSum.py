#constructing list on the go
targetSum=int(input())
nums=list(map(int,input().split()))
dp=[None]*(targetSum+1)
dp[0]=[]
for i in range(targetSum+1):
    if dp[i]!=None:
        for num in nums:
            if i+num<=targetSum:
                if dp[i+num]==None:
                    dp[i+num]=[*dp[i],num]
print(dp[targetSum])
print(dp)


# #my logic backtrack from answer
# targetSum=int(input())
# nums=list(map(int,input().split()))
# dp=[None]*(targetSum+1)
# dp[0]=0
# for i in range(targetSum+1):
#     if dp[i]!=None:
#         for num in nums:
#             if i+num<=targetSum:
#                 dp[i+num]=i
#     if dp[targetSum]!=None:
#         break
# i=targetSum
# result=[]
# while(i>0):
#     result.append(i-dp[i])
#     i=dp[i]
# print(result[::-1])
