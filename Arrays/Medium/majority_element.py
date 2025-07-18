def majority_element(nums):
    count=0
    value=None
    for num in nums:
        if count==0:
            value=num
            count=1
        elif num==value:
            count+=1    
        else:
            count-=1
    return value
nums = list(map(int, input().split()))
print(majority_element(nums))
