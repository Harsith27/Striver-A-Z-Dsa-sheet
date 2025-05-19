n = int(input())
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(chr(64+j),end="")
    for j in range(i,1,-1):
        print(chr(63+j),end="")
    print()


# Pattern
#          A
#        ABA
#      ABCBA
#    ABCDCBA
# ABCDEDCBA