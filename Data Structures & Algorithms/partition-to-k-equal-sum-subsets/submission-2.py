class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        res = False

        if sum(nums) % k != 0:
            return False
        target = int(sum(nums) / k)
        memo = {}

        def dfs(groups):
            key = tuple(sorted(groups))
            if key in memo:
                return memo[key]

            if not nums:
                for g in groups:
                    if g != target:
                        memo[key] = False
                        return False
                memo[key] = True
                return True
            
            
            val = nums.pop()
            for i in range(0, k):
                if groups[i] + val <= target:
                    groups[i] += val
                    if dfs(groups):
                        memo[key] = True
                        nums.append(val)
                        groups[i] -= val
                        return True
                    groups[i] -= val

            nums.append(val)
            memo[key] = False
            return False

        return dfs([0]*k)
