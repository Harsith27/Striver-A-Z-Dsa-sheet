def countSubarrays(nums,k):
    count=0
    seen={0:1}
    curr_sum=0
    for num in nums:
        curr_sum+=num
        if curr_sum-k in seen:
            count+=seen[curr_sum-k]
        seen[curr_sum]=seen.get(curr_sum,0)+1
    return count

nums=[1,2,-1,1,-2,3,1,-2]
k=3
print(countSubarrays(nums,k))
