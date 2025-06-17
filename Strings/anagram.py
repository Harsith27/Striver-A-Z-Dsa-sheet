from collections import Counter
def anagram(s,t):
    return Counter(s)==Counter(t)