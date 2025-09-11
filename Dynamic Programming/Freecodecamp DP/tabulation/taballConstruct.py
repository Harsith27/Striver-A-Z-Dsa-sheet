target=input()
wordBank=list(input().split())
dp=[[] for _ in range(len(target)+1)] 
dp[0]=[[]]
for i in range(len(target)+1):
    if dp[i]!=[]:
        for word in wordBank:
            if target[i:].startswith(word):
                combination=[[*arr,word] for arr in dp[i]]
                dp[i+len(word)].extend(combination)
print(dp[len(target)])
