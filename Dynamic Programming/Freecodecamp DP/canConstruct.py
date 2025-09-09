def canConstruct(target,wordBank):
    if target=="":
        return True
    for word in wordBank:
        if target.startswith(word):
            if canConstruct(target[len(word):],wordBank)==True:
                return True
    return False

target=input()
wordBank=list(input().split())
print(canConstruct(target,wordBank))