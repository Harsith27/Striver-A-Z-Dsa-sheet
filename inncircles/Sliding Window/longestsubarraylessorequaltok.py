def longest_subarray_less_or_equal_to_k(arr,k):
    st=0
    end=0
    currsum=0
    max_len=0
    nums=[]
    while end<len(arr):
        currsum+=arr[end]
        if currsum>k:
            currsum-=arr[st]
            st+=1
        if currsum<=k:
            max_len=max(max_len,end-st+1)
        end+=1
    return max_len
arr=list(map(int,input().split()))
k=int(input())
print(longest_subarray_less_or_equal_to_k(arr,k))