target=input()
wordBank=list(input().split())
dp=[False]*(len(target)+1)
dp[0]=True
for i in range(len(target)+1):
    if dp[i]==True:
        for word in wordBank:
            if target[i:].startswith(word):     # or you can do (target[i:i+len(word)] == word) 
                dp[i+len(word)]=True
            if dp[len(target)]==True:
                break
print(dp[len(target)])

