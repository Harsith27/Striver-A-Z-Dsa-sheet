# n=int(input())
# fib=[0]*(n+1)
# fib[1]=1
# for i in range(2,n+1):
#     fib[i]=fib[i-1]+fib[i-2]
# print(fib[n])

# n=int(input())
# fib=[0]*(n+1)
# fib[1]=1
# for i in range(0,n):
#     fib[i+1]+=fib[i]
#     if (i!=n-1):
#         fib[i+2]+=fib[i]
# print(fib[n])

n=int(input())
lastlast=0
last=1
val=0
for i in range(n-1):
    val=last+lastlast
    lastlast=last
    last=val
print(val)