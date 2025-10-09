def floor_and_ceil(nums,k):
    l,r=0,len(nums)
    while(l<r):
        mid=l+(r-l)//2
        if nums[mid]<k:
            l=mid+1
        else:
            r=mid
    if l < len(nums) and nums[l] == k:
        floor = ceil = nums[l]
    else:
        floor = nums[l-1] if l > 0 else None
        ceil = nums[l] if l < len(nums) else None
    
    return floor, ceil

nums=[3, 4, 4, 7, 8, 10]
k=5
print(floor_and_ceil(nums,k))