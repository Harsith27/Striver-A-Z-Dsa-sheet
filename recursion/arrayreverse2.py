def reverse(arr,n,p1=0,p2=None):
    if p2==None:
        p2=n-1
    if p1>p2:
        return arr
    arr[p1],arr[p2]=arr[p2],arr[p1]
    return reverse(arr,n,p1+1,p2-1)

n=int(input())
arr=list(map(int,input().split()))
print(reverse(arr,n))