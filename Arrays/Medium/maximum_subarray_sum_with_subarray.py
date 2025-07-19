def maximum_subarray_sum_with_subarray(arr):
    start=end=start_temp=0
    curr_sum=0
    max_sum=float('-inf')
    for i in range(len(arr)):
        if arr[i]>curr_sum+arr[i]:
            curr_sum=arr[i]
            start_temp=i
        else:
            curr_sum+=arr[i]
        if curr_sum>max_sum:
            max_sum=curr_sum
            end=i
            start=start_temp
    return [max_sum, arr[start:end+1]]

arr=list(map(int, input().split()))
print(maximum_subarray_sum_with_subarray(arr))