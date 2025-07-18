def two_sum(arr,k):
    seen = {}
    for i in range(len(arr)):
        if k-arr[i] in seen:
            return [seen[k-arr[i]],i]
        seen[arr[i]]=i
        
arr = list(map(int, input().split()))
k=int(input())
print(two_sum(arr,k))
