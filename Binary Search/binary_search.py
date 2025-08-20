def binary_search(arr,k):
    low=0
    high=len(arr)-1
    while(low<high):
        mid=(low+high)//2
        if arr[mid]<k:
            low=mid+1
        elif arr[mid]>k:
            high=mid+1
        else:
            return "element found"

arr=list(map(int,input().split()))
k=int(input())
print(binary_search(arr,k))