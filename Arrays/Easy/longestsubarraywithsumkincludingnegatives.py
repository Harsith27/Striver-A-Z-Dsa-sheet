def longest_subbary_with_sum_k(arr,k):
        prefix_sum=0
        seen={}
        max_len=0
        for i in range(len(arr)):
           prefix_sum+=arr[i]
           if prefix_sum==k:
                   max_len=max(max_len,i+1)
           if prefix_sum-k in seen:
                 max_len=max(max_len,i-seen[prefix_sum-k])
           if prefix_sum not in seen:
                 seen[prefix_sum]=i              
        return max_len
arr=list(map(int, input().split())) 
k = int(input())
print(longest_subbary_with_sum_k(arr,k))