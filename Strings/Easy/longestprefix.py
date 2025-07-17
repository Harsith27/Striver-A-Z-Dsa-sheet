def longestCommonPrefix(strs):
        prefix=""
        for i in range(len(strs[0])):
            char=strs[0][i]
            for word in strs:
                if i>=len(word) or char!=word[i]:
                    return prefix
            prefix+=char
        return prefix
strs=list(input().split())
print(longestCommonPrefix(strs))