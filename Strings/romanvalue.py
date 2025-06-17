def romanToInt(s):
        roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        value=0
        i=len(s)-1
        while(i>=0):
            if i==0:
                value+=roman[s[0]]
                i-=1
            elif roman[s[i]]>roman[s[i-1]]:
                value+=roman[s[i]]-roman[s[i-1]]
                i-=2
            else:
                value+=roman[s[i]]
                i-=1
        return value
s=input()
print(romanToInt(s))