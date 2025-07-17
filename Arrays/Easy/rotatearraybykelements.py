def rotate_array_by_k_elements(arr, k):
    k=k%len(arr)
    arr.reverse()
    arr[:k].reverse()
    arr[k:len(arr)].reverse()
    return arr

arr = list(map(int, input().split()))
k = int(input())
print(rotate_array_by_k_elements(arr, k))