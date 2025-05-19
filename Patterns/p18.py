n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+(n-i)+j),end="")
    print()



# Pattern
# E
# DE
# CDE
# BCDE
# ABCDE
   
# Explanation
#     A=65
#     B=66
#     C=67
#     D=68
#     E=69

#     i=1,2,3,4,5

# 64+(n-i)+j

#     E=69
#     D E = 68 69
#     C D E= 67 68 69
#     B C D E= 66 67 68 69
#     A B C D E=65 66 67 68 69