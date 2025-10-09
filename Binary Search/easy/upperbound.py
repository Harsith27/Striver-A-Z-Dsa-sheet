def upperbound(arr,k):
    l,r=0,len(arr)
    while(l<r):
        mid=l+(r-l)//2
        if arr[mid]<=k:
            l=mid+1
        else:
            r=mid
    return l
arr=[1,2,4,4,4,5,6]
k=4
print(upperbound(arr,k))