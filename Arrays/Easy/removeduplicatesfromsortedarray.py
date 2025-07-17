def remove_duplicates_from_sorted_array(arr):
    i=0
    for j in range(len(arr)):
        if arr[j]!=arr[i]:
            i+=1
            arr[i]=arr[j]
    return arr[:i+1]

arr=list(map(int,input().split()))
print(remove_duplicates_from_sorted_array(arr))