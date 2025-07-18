def sortColors(nums):
    colors = [0, 0, 0]
    for i in nums:
        if i==0:
            colors[0]+=1
        elif i==1:
            colors[1]+=1
        else:
            colors[2]+=1
    k=0
    for i in range(len(nums)):
        while colors[k]==0:
            k+=1
        nums[i]=k
        colors[k]-=1
    return nums

nums = list(map(int, input().split()))
print(sortColors(nums))


#same logic but diff way of writing 
def sortColors(nums):
    count0 = nums.count(0)
    count1 = nums.count(1)
    count2 = nums.count(2)
    nums[:] = [0]*count0 + [1]*count1 + [2]*count2
    return nums

nums = list(map(int, input().split()))
print(sortColors(nums))



