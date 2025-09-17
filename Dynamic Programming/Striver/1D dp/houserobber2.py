def houserobber2(n,nums):
    if n<0:
        return 0
    if n==0:
        return nums[0]
    rob=houserobber2(n-2,nums)+nums[n]
    skip=houserobber2(n-1,nums)
    return max(rob,skip)
nums=list(map(int,input().split()))
firstway=houserobber2(len(nums[:len(nums)-1])-1,nums[:len(nums)-1])
secondway=houserobber2(len(nums[1:len(nums)])-1,nums[1:len(nums)])
print(max(firstway,secondway))
