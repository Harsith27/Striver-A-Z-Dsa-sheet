def linearsearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return f"found at index {i}"
    return "not found"
arr = list(map(int, input().split()))
target = int(input())
print(linearsearch(arr, target))