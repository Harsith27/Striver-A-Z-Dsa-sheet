def ksumsubarray(arr,k):
    total_sum=sum(arr[:k])
    max_sum=total_sum
    for i in range(1,len(arr)-k+1):
        total_sum=total_sum-arr[i-1]+arr[i+k-1]
        max_sum=max(max_sum,total_sum)
    return max_sum
arr=list(map(int,input().split()))
k=int(input())
print(ksumsubarray(arr,k))
