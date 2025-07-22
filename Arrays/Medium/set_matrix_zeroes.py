def set_matrix_zeroes(matrix,n,m):
    first_row=False
    first_col=False
    for j in range(m):
        if matrix[j][0]==0:
            first_row=True
            break
    for i in range(n):
        if matrix[0][i]==0:
            first_col=True
            break
    for i in range(1,n):
        for j in range(1,m):
            if matrix[i][j]==0:
                matrix[i][0]=0
                matrix[0][j]=0
    for i in range(1,n):
        for j in range(1,m):
            if matrix[i][0]==0 or matrix[0][j]==0:
                matrix[i][j]=0
    if first_row:
        for j in range(n):
            matrix[0][j]=0 
    if first_col:
        for i in range(n):
            matrix[i][0]=0
    return matrix

n,m=map(int,input().split())
matrix=[list(map(int,input().split())) for _ in range(n)]
print(set_matrix_zeroes(matrix,n,m))