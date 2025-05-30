def fib_nterms(n,a=0,b=1,count=0):
    if count==n:
        return 
    print(a,end=" ")
    return fib_nterms(n,b,a+b,count+1)

n=int(input())
fib_nterms(n)


#iterative case

# def fib_nterms(n):
#     arr=[0,1]
#     print(*arr,end=" ")
#     for _ in range(2,n):
#         result=(arr[0]+arr[1])
#         print(result,end=" ")
#         arr[0]=arr[1]
#         arr[1]=result

# n=int(input())
# fib_nterms(n)