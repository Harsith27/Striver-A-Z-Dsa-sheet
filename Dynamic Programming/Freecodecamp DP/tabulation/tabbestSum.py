targetSum=int(input())
nums=list(map(int,input().split()))
dp=[None]*(targetSum+1)
dp[0]=[]
for i in range(targetSum+1):
    if dp[i]!=None:
        for num in nums:
            if i+num<=targetSum:
                val=[*dp[i],num]
                if (dp[i+num] is None or (len(dp[i+num])>len(val))):
                    dp[i+num]=val
print(dp[targetSum])

