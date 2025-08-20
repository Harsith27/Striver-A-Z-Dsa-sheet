def min_in_rot_sorted_array(arr):
    l,r=0,len(arr)-1
    while(l<r):
        mid=l+(r-l)//2
        if arr[mid]>arr[mid+1]:
            return arr[mid+1]
        if arr[mid]>arr[r]:
            l=mid+1
        else:
            r=mid

arr=list(map(int,input().split()))
print(min_in_rot_sorted_array(arr))