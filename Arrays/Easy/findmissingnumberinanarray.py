def find_missing_number_in_array(arr):
    n = len(arr)   # Since one number is missing
    total_sum = n * (n + 1) // 2    
    array_sum = sum(arr)
    return total_sum - array_sum
arr = list(map(int, input().split()))
print(find_missing_number_in_array(arr))

# #another approach using XOR
def find_missing_number_xor(arr):
    n = len(arr) 
    xor_all = 0
    xor_arr = 0
    for i in range(n+1):
        xor_all ^= i 
    for num in arr:
        xor_arr ^= num  
    return xor_all ^ xor_arr

arr = list(map(int, input().split()))
print(find_missing_number_xor(arr))