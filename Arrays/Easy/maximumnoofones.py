def maximum_no_of_ones(arr):
    count = 0
    max_count = 0
    for num in arr:
        if num==1:
            count+=1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count

arr = list(map(int, input().split()))
print(maximum_no_of_ones(arr))