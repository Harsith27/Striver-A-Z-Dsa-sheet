def lowerbound(arr,k):
    l=0
    r=len(arr)
    while(l<r):
        mid=l+(r-l)//2
        if arr[mid]<k:
            l=mid+1
        else:
            r=mid
    return l

arr=list(map(int,input().split()))
k=int(input())
print(lowerbound(arr,k))