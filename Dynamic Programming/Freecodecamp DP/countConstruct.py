def countConstruct(target,wordBank):
    if target=="":
        return 1
    totalways=0
    for word in wordBank:
        if target.startswith(word):
            suffix=target[len(word):]
            ways=countConstruct(suffix,wordBank)
            totalways+=ways
    return totalways
        
target=input()
wordBank=list(input().split())
print(countConstruct(target,wordBank))