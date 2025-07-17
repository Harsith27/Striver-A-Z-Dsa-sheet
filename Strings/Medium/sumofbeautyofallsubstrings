from collections import Counter
def sumofbeauty(s):
    total=0
    beauty=0
    for i in range(len(s)):
        freq=Counter()
        for j in range(i, len(s)):
            freq[s[j]] += 1
            beauty=max(freq.values()) - min(freq.values())
            total+=beauty
    return total
s=input()
print(sumofbeauty(s))