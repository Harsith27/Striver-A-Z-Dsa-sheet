def reverse(arr,p1,p2):
    if p1>p2:
        return arr
    arr[p1],arr[p2]=arr[p2],arr[p1]
    return reverse(arr,p1+1,p2-1)

n=int(input())
arr=list(map(int,input().split()))
print(reverse(arr,0,n-1))