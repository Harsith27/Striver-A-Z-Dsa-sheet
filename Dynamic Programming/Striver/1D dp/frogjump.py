def frogjump(n,nums):
    if n==0:
        return 0
    if n==1:
        return abs(nums[1]-nums[0])
    jump1=frogjump(n-1,nums)+abs(nums[n]-nums[n-1])
    jump2=frogjump(n-2,nums)+abs(nums[n]-nums[n-2])
    return min(jump1,jump2)
nums=list(map(int,input().split()))
print(frogjump(len(nums)-1,nums))