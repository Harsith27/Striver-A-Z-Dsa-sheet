n=int(input())
for i in range(n,0,-1):
    for j in range(0,i):
        print(chr(65+j),end="")
    print()
    

# pattern
# ABCDE
# ABCD
# ABC
# AB
# A