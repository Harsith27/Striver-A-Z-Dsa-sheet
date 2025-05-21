def arrayreverse(arr,n,copy=[]):
    if n==0:
        return copy
    copy.append(arr[n-1])
    return arrayreverse(arr,n-1,copy)

n=int(input())
arr=list(map(int,input().split()))
print(arrayreverse(arr,n))
