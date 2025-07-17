arr=list(map(int,input().split()))
flag=True
for i in range(1,len(arr)):
    if arr[i]<arr[i-1]:
        flag=False
        break  
print(flag)