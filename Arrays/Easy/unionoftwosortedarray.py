def union_of_two_sorted_arrays(arr1, arr2):
    i,j=0,0
    res=[]
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            if arr1[i] not in res:  #check is there cuz in union we don't want duplicates
                res.append(arr1[i])  #and this is used only for when an array has its own dupliactes
            i+=1
        elif arr1[i]>arr2[j]:
            if arr2[j] not in res: 
                res.append(arr2[j])
            j+=1
        else:
            if arr1[i] not in res:   # when both are equal we only need to consider one and increment both i and j
                res.append(arr1[i]) 
            i+=1
            j+=1
    while i<len(arr1):
        if arr1[i] not in res:
            res.append(arr1[i])
        i+=1
    while j<len(arr2):
        if arr2[j] not in res:
            res.append(arr2[j])
        j+=1        
    return res

arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
print(union_of_two_sorted_arrays(arr1, arr2))
#This approach has o((n+m)^2) time complexity
#use sets to reduce time complexity to O(n+m) by reducing membership checks to O(1)  but space will be more