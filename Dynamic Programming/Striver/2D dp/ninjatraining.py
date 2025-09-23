#Time optimized 
def ninjatraining(n,points):
    dp=[[0]*3 for _ in range(n)]
    for i in range(n):
        dp[0][i]=points[0][i]
    for day in range(1,n):
        for i in range(3):
            prev_best=0
            for j in range(3):
                if i!=j:
                    prev_best=max(prev_best,dp[day-1][j])
            dp[day][i]=prev_best+points[day][i]
    print(dp)
    return max(dp[n-1])

n=3
points = [
    [10, 40, 70],
    [20, 50, 80],
    [30, 60, 90]
]
print(ninjatraining(n,points))

#Space optimization - O(n)

def ninjatraining(n,points):
    prev=[0]*3
    for i in range(3):
        prev[i]=points[0][i]
    for day in range(1,n):
        curr=[0]*3
        for i in range(3):
            prev_best=0
            for j in range(3):
                if i!=j:
                    prev_best=max(prev_best,prev[j])
            curr[i]=prev_best+points[day][i]
        prev=curr
        print(prev,curr)
    return max(prev)    # or return max(curr)

n=3
points = [
    [10, 40, 70],
    [20, 50, 80],
    [30, 60, 90]
]
print(ninjatraining(n,points))