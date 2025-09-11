#push forward
r,c=map(int,input().split())
grid=[[0]*c for i in range(r)]
for i in range(r):
    for j in range(c):
        if i==0 and j==0:
            grid[i][j]=1
        if j<c-1:
            grid[i][j+1]+=grid[i][j]
        if i<r-1:
            grid[i+1][j]+=grid[i][j]
print(grid[r-1][c-1])
    

#pull from past
r,c=map(int,input().split())
grid=[[0]*(c+1) for i in range(r+1)]
grid[1][1]=1
for i in range(1,r+1):
    for j in range(1,c+1):
        if i ==1 and j == 1:
            continue
        grid[i][j]=grid[i][j-1]+grid[i-1][j]

print(grid)