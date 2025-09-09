def allConstruct(target,wordBank):
    if target=="":
        return [[]]
    result=[]
    for word in wordBank:
        if target.startswith(word):
            suffix=target[len(word):]
            suffixways=allConstruct(suffix,wordBank)
            targetways=[[word,*way] for way in suffixways]
            result.extend(targetways)
    return result
        
target=input()
wordBank=list(input().split())
print(allConstruct(target,wordBank))
             
