arr=list(map(int,input().split()))
max_ele=arr[0]
for i in range(1,len(arr)):
    if arr[i]>max_ele:
        max_ele=arr[i]  
print(max_ele)