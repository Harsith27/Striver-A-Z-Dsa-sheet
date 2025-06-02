# 1) freaquency of numbers

# #Appraoch 1
# arr=list(map(int,input().split()))
# mydict={}
# for num in arr:
#     mydict[num]=mydict.get(num,0)+1
# print(mydict)

#Approach 2
# from collections import Counter
# arr=list(map(int,input().split()))
# freq=Counter(arr)
# print(freq)

#-------------------------------------------------------------------------------------------------------------------------
# #2) Invert a dictioanry's keys and values

# Approach1--------------------------------
# newdict={"a":1,"b":2,"c":3}
# newdict=dict(zip(newdict.values(),newdict.keys()))
# print(newdict)

# Approach 2---------------------------------
# newdict={"a":1,"b":2,"c":3}
# newdict={v:k for k,v in newdict.items()}
# print(newdict)

# #3) group words by first letter in dict
# words = ["apple", "banana", "apricot", "cherry", "blueberry"]
# group={}
# for word in words:
#     ch=word[0]
#     if ch in group:
#         group[ch].append(word)
#     else:
#         group[ch]=[word]
# print(group)


# #5) sort a dict based on its keys
# d = {'banana': 3, 'apple': 4, 'cherry': 2}
# sorted_dict = {}  
# for key in sorted(d.keys()):
#     sorted_dict[key] = d[key] 
# print(sorted_dict)

# #6) sort a dict based on its values

#Approach 1
# d = {'banana': 3, 'apple': 4, 'cherry': 2}
# newd={v:k for k,v in d.items()}
# sorted_dict={}
# for key in sorted(newd.keys()):
#     sorted_dict[newd[key]]=key
# print(sorted_dict)

#NOTE:: doesm't wark for dicttionary having duplicate values
#Approach 2(lamnda)
# d = {'banana': 3, 'apple': 4, 'cherry': 2}


