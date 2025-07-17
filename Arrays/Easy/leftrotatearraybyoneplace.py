def left_rotate_array_by_one_place(arr):
    temp=arr[0]
    for i in range(len(arr)-1):
        arr[i]=arr[i+1]
    arr[-1]=temp
    return arr
arr=list(map(int,input().split()))
print(left_rotate_array_by_one_place(arr))
