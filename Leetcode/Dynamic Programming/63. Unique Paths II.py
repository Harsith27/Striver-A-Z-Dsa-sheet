class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        def helper(i, j, memo={}):
            if i < 0 or j < 0:
                return 0
            if obstacleGrid[i][j] == 1:
                return 0
            if i == 0 and j == 0:
                return 1
            key = (i, j)
            if key in memo:
                return memo[key]
            memo[key] = helper(i - 1, j, memo) + helper(i, j - 1, memo)
            return memo[key]

        return helper(n - 1, m - 1)
