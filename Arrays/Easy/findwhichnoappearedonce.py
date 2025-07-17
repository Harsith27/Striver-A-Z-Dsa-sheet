def find_which_no_appear_once(arr):
    xor=0
    for num in arr:
        xor^=num
    return xor


arr = list(map(int, input().split()))
print(find_which_no_appear_once(arr))