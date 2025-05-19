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