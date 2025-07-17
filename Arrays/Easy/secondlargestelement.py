arr=list(map(int,input().split()))
max_ele=float('-inf')
second_max_ele=float('-inf')
for i in range(len(arr)):
    if arr[i] > max_ele:
        second_max_ele = max_ele
        max_ele = arr[i]        
print(second_max_ele)