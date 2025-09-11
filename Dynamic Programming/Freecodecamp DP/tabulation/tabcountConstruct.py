target=input()
wordBank=list(input().split())
dp=[0]*(len(target)+1)
dp[0]=1
for i in range(len(target)+1):
    if dp[i]!=0:
        for word in wordBank:
            if target[i:].startswith(word):
                dp[i+len(word)]+=dp[i]
print(dp)
print(dp[len(target)])