def rotate_array_by_k_elements(arr, k):
    k=k%len(arr)
    arr.reverse()
    arr[:k] = reversed(arr[:k])  # Reverse first k elements
    arr[k:] = reversed(arr[k:]) # Reverse the rest of the elements
    return arr

arr = list(map(int, input().split()))
k = int(input())
print(rotate_array_by_k_elements(arr, k))