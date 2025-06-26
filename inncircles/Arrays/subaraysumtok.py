def subarraysum(arr, k):
    prefix = {0: 1}
    count = 0
    curr_sum = 0

    for num in arr:
        curr_sum += num
        if curr_sum - k in prefix:
            count += prefix[curr_sum - k]
        prefix[curr_sum] = prefix.get(curr_sum, 0) + 1

    return count

arr=list(map(int,input().split()))
k=int(input())
print(subarraysum(arr,k))
