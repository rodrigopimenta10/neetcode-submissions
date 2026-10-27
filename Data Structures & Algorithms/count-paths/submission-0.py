class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dfs(i,j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            elif i == m-1 and j == n-1:
                return 1
            elif (i,j) in memo:
                return memo[(i,j)]
            
            memo[(i,j)] = dfs(i+1,j) + dfs(i,j+1)
            return memo[(i,j)]

        return dfs(0,0)