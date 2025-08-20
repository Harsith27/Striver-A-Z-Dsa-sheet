def floor_and_ceil_of_target(arr,k):
    l,r=0,len(arr)-1
    while(l<=r):
        mid=l+(r-l)//2
        if arr[mid]>k:
            r=mid-1
        elif arr[mid]<k:
            l=mid+1
        else:
            return arr[mid]
    return False

def lowerbound(arr,k):
    l=0
    r=len(arr)
    while(l<r):
        mid=l+(r-l)//2
        if arr[mid]<k:
            l=mid+1
        else:
            r=mid
    return arr[l-1]
    

def upperbound(arr,k):
    l,r=0,len(arr)
    while(l<r):
        mid=l+(r-l)//2
        if arr[mid]<=k:
            l=mid+1
        else:
            r=mid
    return arr[l]


arr=list(map(int,input().split()))
k=int(input())
ans=floor_and_ceil_of_target(arr,k)
if ans!=False:
    print(ans,ans)
else:
    print(lowerbound(arr,k), upperbound(arr,k))