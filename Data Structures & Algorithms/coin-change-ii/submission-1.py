class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(i, x):
            if x == 0:
                return 1
            if x < 0 or i == len(coins):
                return 0
            if (i, x) in memo:
                return memo[(i, x)]
            
            total = 0
            for j in range(0, x // coins[i] + 1):
                total += dfs(i + 1, x - j * coins[i])
            memo[(i, x)] = total
            return total

        return dfs(0, amount)
