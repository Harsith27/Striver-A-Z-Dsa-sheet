def longest_consecutive_sequence(arr):
    myset=set(arr)
    max_len=0
    start=None
    for num in arr:
        curr=num
        while curr in myset:
            curr+=1
        length=curr-num
        if length>max_len:
            max_len=length
            start=num
    return [start+i for i in range(max_len)]

arr=list(map(int, input().split()))
print(longest_consecutive_sequence(arr))