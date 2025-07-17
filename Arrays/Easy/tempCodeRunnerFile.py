
# #another approach using XOR
# def find_missing_number_xor(arr):
#     n = len(arr) + 1
#     xor_all = 0
#     xor_arr = 0
#     for i in range(n):
#         xor_all^=i+1
#         xor_arr^=arr[i]
#     xor_all^=n
#     return xor_all ^ xor_arr
# arr = list(map(int, input().split()))
# print(find_missing_number_xor(arr))