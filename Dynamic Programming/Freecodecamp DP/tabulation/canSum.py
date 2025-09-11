targetSum=int(input())
nums=list(map(int,input().split()))
dp=[False]*(targetSum+1)
dp[0]=True  #default case
for i in range(targetSum+1):
    if dp[i]==True:            
        for num in nums:
            if i+num<=targetSum:
                dp[i+num]=True
print(dp)
print(dp[targetSum])