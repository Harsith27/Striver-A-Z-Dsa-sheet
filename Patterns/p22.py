n=int(input())
print((str(n)+" ")*((n*2)-1))
for i in range(1, n):
    for j in range(i):
        print(n - j, end=" ")
    print((str(n-i)+" ")*(((n-i)*2)-1),end="")
    for j in range(1,i+1):
        print((n-i)+j,end=" ")
    print()

for i in range(n-2 , 0, -1):
    for j in range(i):
        print(n - j, end=" ")
    print((str(n-i)+" ")*(((n-i)*2)-1),end="")
    for j in range(1,i+1):
        print(n-i+j,end=" ")
    print()
print((str(n)+" ")*((n*2)-1))



# Pattern
# 4 4 4 4 4 4 4 
# 4 3 3 3 3 3 4 
# 4 3 2 2 2 3 4 
# 4 3 2 1 2 3 4 
# 4 3 2 2 2 3 4
# 4 3 3 3 3 3 4
# 4 4 4 4 4 4 4














# n=int(input())
# for i in range(n,0,-1):
#     for j in range(n,i-1,-1):
#         print(j,end="")
#     for k in range((i-1)*2):
#         print(i,end="")
#     for j in range(i,n+1):
#         print(j,end="")
#     print()
# for i in range(n-1):
#     num=n
#     for j in range(n - i -1):
#         print(num, end="")
#         num -= 1
#     val=i+2
#     for k in range((i+1)*2):
#         print(val,end="")
    
#     print()