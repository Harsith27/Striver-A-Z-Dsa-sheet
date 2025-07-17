def merge_two_sorted_arrays(arr1,arr2):
    i,j=0,0
    res=[]
    while(i<len(arr1)) and (j<len(arr2)):
        if arr1[i]<arr2[j]:
            res.append(arr1[i])
            i+=1
        else:
            res.append(arr2[j])
            j+=1
    while i<len(arr1):
        res.append(arr1[i])
        i+=1
    while j<len(arr2):
        res.append(arr2[j])
        j+=1
    return res

arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
print(merge_two_sorted_arrays(arr1, arr2))
