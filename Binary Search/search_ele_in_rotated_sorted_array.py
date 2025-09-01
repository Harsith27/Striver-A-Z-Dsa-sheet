def search_ele_in_rotated_sorted_array(nums,k):
    l,r=0,len(nums)-1
    while(l<=r):
        mid=l+(r-l)//2
        if nums[mid]==k:
            return mid
        if nums[l]<=nums[mid]:
            if nums[l]<=k<nums[mid]:
                r=mid-1
            else:
                l=mid+1
        else:
            if nums[mid]<k<=nums[r]:
                l=mid+1
            else:
                r=mid-1
    return -1

nums=list(map(int,input().split()))
k=int(input())
print(search_ele_in_rotated_sorted_array(nums,k))
 