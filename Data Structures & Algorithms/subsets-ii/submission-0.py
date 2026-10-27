class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = set()
        returned = []

        def dfs(i, combo):
            if i == len(nums):
                #combo.sort()
                result.add(tuple(sorted(combo)))
                return
            combo.append(nums[i])
            dfs(i + 1, combo)
            combo.pop()
            dfs(i + 1, combo)

        
        dfs(0, [])
        for s in result:
            returned.append(list(s))
        return returned


