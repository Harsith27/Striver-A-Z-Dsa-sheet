def sort_colors_2(arr):
    l=0
    m=0
    h=len(arr)-1
    while m<=h:
        if arr[m]==0:
            arr[m],arr[l]=arr[l],arr[m]
            m+=1
            l+=1
        elif arr[m]==2:
            arr[m],arr[h]=arr[h],arr[m]
            h-=1
        else:
            m+=1
    return arr
arr=list(map(int, input().split()))
print(sort_colors_2(arr))


