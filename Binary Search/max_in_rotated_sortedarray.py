def max_rotated_sorted_array(arr):
    l,r=0,len(arr)-1
    while(l<r):
        mid=l+(r-l)//2
        # check for maximum
        if arr[mid]>arr[mid+1]:  
            return arr[mid]
        # decide search space
        if arr[mid]>arr[r]:
            l=mid+1
        else:
            r=mid-1

# this fails for when array is 1

arr=list(map(int,input().split()))
print(max_rotated_sorted_array(arr))
