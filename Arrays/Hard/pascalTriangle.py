def pascal_triangle(n):
    res=[[1]]
    for i in range(1,n):
        row=[1]+[res[i-1][j-1]+res[i-1][j] for j in range(1,i)]+[1]
        res.append(row)
    return res

n=6
print(pascal_triangle(n))

# def pascal_triangle(n):
#     res=[[1]]
#     if n==1:
#         return res
#     for i in range(2,n+1):
#         level=[0]*i
#         level[0]=1
#         level[i-1]=1
#         for j in range(1,i-1):
#             level[j]=res[i-2][j]+res[i-2][j-1]
#         res.append(level)
#     return res

# n=6
# res=pascal_triangle(n)
# for level in res:
#     print(level)  

