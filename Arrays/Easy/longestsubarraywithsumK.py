def longestsubarraywithsumK(arr):
    j=0
    sum=0
    max_length=0
    for i in range(len(arr)):   
        sum+=arr[i]
        while sum > k:
            sum -= arr[j]
            j += 1
        if sum == k:
            max_length = max(max_length, i - j + 1)
    return max_length   
arr=list(map(int, input().split()))
k = int(input())
print(longestsubarraywithsumK(arr))