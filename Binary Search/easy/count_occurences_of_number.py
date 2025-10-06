def firstoccurence(arr,k):
    l,r=0,len(arr)
    while(l<r):
        mid=l+(r-l)//2
        if arr[mid]<k:
            l=mid+1
        else:
            r=mid
    return l

def lastoccurence(arr,k):
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
print("count -",lastoccurence(arr,k)-firstoccurence(arr,k))


# remember to do code reuse as well
# def bound(arr, k, find_first):
#     l, r = 0, len(arr)
#     while l < r:
#         mid = l + (r - l) // 2
#         if arr[mid] < k or (not find_first and arr[mid] == k):
#             l = mid + 1
#         else:
#             r = mid
#     return l

# def firstoccurence(arr, k):
#     return bound(arr, k, True)

# def lastoccurence(arr, k):
#     return bound(arr, k, False)