def max_rotated_sorted_array(arr):
    low=0
    high=len(arr)-1
    while(low<high):
        mid=(low+high)//2
        if arr[mid]<arr[mid+1]:
            low=mid+1
        elif arr[mid]>arr[mid+1]:
            high=mid
    return arr[low]

arr=list(map(int,input().split()))
print(max_rotated_sorted_array(arr))
