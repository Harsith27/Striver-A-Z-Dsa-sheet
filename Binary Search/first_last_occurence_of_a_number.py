def firstoccurence(arr,k):
    l,r=0,len(arr)-1
    while(l<r):
        mid=l+(r-l)//2
        if arr[mid]<k:
            l=mid+1
        else:
            r=mid
    return l

def lastoccurence(arr,k):
    l,r=0,len(arr)-1
    while(l<r):
        mid=l+(r-l)//2
        if arr[mid]<=k:
            l=mid+1
        else:
            r=mid
    return l

arr=list(map(int,input().split()))
k=int(input())
print(firstoccurence(arr,k),lastoccurence(arr,k))
