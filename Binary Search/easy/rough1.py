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
    return "element Not found"

arr=[1,2,3,4,5,6,7]
k=3
print(binary_search(arr,k))