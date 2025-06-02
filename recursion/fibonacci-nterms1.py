def fib_nterms(n,arr=[0,1]):
    if n==1:
        return [0]
    if len(arr)>=n:
        return arr
    arr.append(arr[-1]+arr[-2])
    return fib_nterms(n,arr)

n=int(input())
print(*fib_nterms(n))



# Iterative approach

# def fib_nterms(n,arr):
#     for i in range(2,n):
#         arr.append(arr[i-1]+arr[i-2])
#     return arr
# n=int(input())
# arr=[0,1]
# print(*fib_nterms(n,arr))

