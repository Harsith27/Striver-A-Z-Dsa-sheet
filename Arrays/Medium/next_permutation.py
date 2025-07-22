def next_permutation(arr):
    n=len(arr)
    i=n-2
    while i>=0 and arr[i]>=arr[i+1]:
        i-=1
    if i>=0:
        j=n-1
        while arr[j]<=arr[i]:
            j-=1
        arr[i],arr[j]=arr[j],arr[i]
    arr[i+1:]=list(reversed(arr[i+1:]))
    print(arr)


arr=list(map(int, input().split()))
next_permutation(arr)