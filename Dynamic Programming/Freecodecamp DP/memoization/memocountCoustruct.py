def countConstruct(target,wordBank,memo={}):
    if target=="":
        return 1
    if target in memo:
        return memo[target]
    totalWays=0
    for word in wordBank:
        if target.startswith(word):
            suffix=target[len(word):]
            ways=countConstruct(suffix,wordBank,memo)
    memo[target]=totalWays
    return memo[target]
        
target=input()
wordBank=list(input().split())
print(countConstruct(target,wordBank))
