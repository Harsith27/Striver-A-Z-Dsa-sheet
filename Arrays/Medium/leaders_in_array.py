def leaders_in_array(arr):
    max_val=arr[len(arr)-1]
    arr[len(arr)-1]=1
    for i in range(len(arr)-2,-1,-1):
        if arr[i]>max_val:
            max_val=arr[i]
            arr[i]=1
        else:
            arr[i]=0
    return arr
arr=list(map(int,input().split()))
print(leaders_in_array(arr))