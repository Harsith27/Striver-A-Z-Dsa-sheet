def longest_subarray_with_equal0and1(arr):
    arr=[-1 if x==0 else 1 for x in arr]
    prefix={0:-1}
    curr=0
    max_len=0
    for i in range(len(arr)):
        curr+=arr[i]
        if curr in prefix:
            max_len=max(max_len,i-prefix[curr])
        else:
            prefix[curr]=i
    return max_len
arr=list(map(int,input().split()))
print(longest_subarray_with_equal0and1(arr))