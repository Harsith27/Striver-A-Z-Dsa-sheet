def rotatematrix(matrix,n):
    k=0
    for i in range(1,n):
        for j in range(i):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
    return matrix

n=(int(input()))
matrix=[list(map(int,input().split())) for _ in range(n)]
print(rotatematrix(matrix,n))