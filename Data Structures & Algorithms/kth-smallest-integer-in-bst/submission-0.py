# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums = []

        def dfs(cur):
            nonlocal nums
            if cur == None:
                return
            heapq.heappush(nums, cur.val)
            dfs(cur.left)
            dfs(cur.right)
            return

        dfs(root)
        #print(nums)

        i = 0
        while i < k:
            res = heapq.heappop(nums)
            i += 1
        return res


