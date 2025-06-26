def longest_subarray_to_k_len(arr, k):
    prefix={0:-1}
    curr=0
    max_len=0
    for i in range(len(arr)):
        curr+=arr[i]
        if curr==k:
            max_len=i+1
        if (curr-k) in prefix:
            max_len=max(max_len,prefix[curr-k])
        if curr not in prefix:
            prefix[curr]=i
    return max_len
arr=list(map(int,input().split()))
k=int(input())
print(longest_subarray_to_k_len(arr,k))