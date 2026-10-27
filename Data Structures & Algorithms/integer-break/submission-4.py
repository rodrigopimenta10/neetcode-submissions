class Solution:
    def integerBreak(self, n: int) -> int:
        #self.res = 0
        memo = {}
        def dfs(x):
            if x in memo:
                return memo[x]
            if x == 1:
                return 1
            res = 0
            for i in range(1,x):
                res = max(res, i*dfs(x-i), i*(x-i))
            memo[x] = res
            return res

        return dfs(n)
        