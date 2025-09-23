# import math
class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         return math.factorial(m+n-2)//(math.factorial(m-1)*factorial(n-1))
    def uniquePaths(self, m: int, n: int,memo={}) -> int:
        if m==0 or n==0:
            return 0 
        if m==1 and n==1:
            return 1
        key=(max(m,n),min(m,n))
        if key in memo:
            return memo[key]
        memo[key]=self.uniquePaths(m-1,n,memo)+self.uniquePaths(m,n-1,memo)
        return memo[key]