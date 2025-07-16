s=input()
s=s.lstrip('0')
for i in range(len(s)-1,-1,-1):
    if int(s[i])%2!=0:
        print(s[0:i+1])
        break
