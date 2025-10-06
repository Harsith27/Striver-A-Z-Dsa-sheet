def upperbound(arr,k):
    l,r=0,len(arr)
    while(l<r):
        mid=l+(r-l)//2
        if arr[mid]<=k:
            l=mid+1
        else:
            r=mid
    return l
arr=list(map(int,input().split()))
k=int(input())
print(upperbound(arr,k))