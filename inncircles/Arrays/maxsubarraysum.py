#kadanes Algorithm
def maxsubarraysum(arr):
    curr=0
    maxsum=float('-inf')
    for num in arr:
        curr=max(num,curr+num)
        maxsum=max(maxsum,curr)
        print(maxsum,curr)
    return maxsum
arr=list(map(int,input().split()))
print(arr)
print(maxsubarraysum(arr))