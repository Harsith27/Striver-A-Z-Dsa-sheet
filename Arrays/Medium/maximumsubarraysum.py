def maximum_subarray_sum(arr):
    curr_sum=0
    max_sum=float('-inf')
    for num in arr:
        curr_sum=max(num, curr_sum + num)
        max_sum=max(max_sum, curr_sum)
    return max_sum
arr=list(map(int, input().split()))
print(maximum_subarray_sum(arr))