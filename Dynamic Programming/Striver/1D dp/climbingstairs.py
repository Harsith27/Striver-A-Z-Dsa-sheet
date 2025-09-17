def climbingStairs(n,memo={}):
    if n<=2:
        return n
    if n in memo:
        return memo[n]
    memo[n]=climbingStairs(n-1,memo)+climbingStairs(n-2,memo)
    return memo[n]

n=int(input())
print(climbingStairs(n))