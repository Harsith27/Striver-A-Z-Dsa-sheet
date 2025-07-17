def myAtoi(s):
        sign=1
        ans=""
        flag=0
        for i in range(len(s)):
            if s[i]==" " and flag==0:
                continue
            if s[i]=="-" and flag==0:
                sign=-1
                flag=1
                continue
            if s[i]=="+" and flag==0:
                flag=1
                continue
            if s[i].isdigit():
                ans+=s[i]
                flag=1
            else:
                break
        if not ans:
            return 0
        ans=int(ans)*sign
        INT_MIN=-2**31
        INT_MAX=2**31-1
        if ans>INT_MAX:
            return INT_MAX
        if ans<INT_MIN:
            return INT_MIN
        return ans
s=input()
print(myAtoi(s))