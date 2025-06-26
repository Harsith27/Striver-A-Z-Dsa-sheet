def smallest_subarray_greater_or_equal_to_k(arr, k):
    st = 0
    end = 0
    currsum = 0
    min_len = float('inf')
    while end < len(arr):
        currsum += arr[end]
        while currsum >= k and st <= end:
            min_len = min(min_len, end - st + 1)
            currsum -= arr[st]
            st += 1
        end += 1
    return 0 if min_len == float('inf') else min_len

arr=list(map(int,input().split()))
k=int(input())
print(smallest_subarray_greater_or_equal_to_k(arr,k))
