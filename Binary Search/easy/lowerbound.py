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
arr=[1,2,4,4,4,5,6,7]
k=8
print(lowerbound(arr,k))