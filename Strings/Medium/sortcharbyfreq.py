from collections import Counter
def frequencySort(s):
    freq=Counter(s)
    sorteddict=dict(sorted(freq.items(), key=lambda item: (-item[1],item[0])))
    s=""
    for i in sorteddict.keys():
        s=s+(i)*sorteddict[i]
    return s

s=input()
print(frequencySort(s))
