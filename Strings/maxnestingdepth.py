def maxDepth(s):
        count=0
        max=0
        for i in s:
            if i=="(":
                count+=1
                if count>max:
                    max=count
            elif i==")":
                count-=1
        return max
s=input()
print(maxDepth(s))