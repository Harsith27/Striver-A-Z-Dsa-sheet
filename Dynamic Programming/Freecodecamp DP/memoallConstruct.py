def allConstruct(target,wordBank,memo={}):
    if target=="":
        return [[]]
    if target in memo:
        return memo[target]
    result=[]
    for word in wordBank:
        if target.startswith(word):
            suffix=target[len(word):]
            suffixways=allConstruct(suffix,wordBank,memo)
            targetways=[[word,*way] for way in suffixways]
            result.extend(targetways)
    memo[target]=result
    return memo[target]

target=input()
wordBank=list(input().split())
print(allConstruct(target,wordBank))
        