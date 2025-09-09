def canConstruct(target,wordBank,memo={}):
    if target=="":
        return True
    if target in memo:
        return memo[target]
    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            if canConstruct(suffix,wordBank)==True:
                memo[target]=True
    memo[target]=False
    return memo[target]

target=input()
wordBank=list(input().split())
print(canConstruct(target,wordBank))