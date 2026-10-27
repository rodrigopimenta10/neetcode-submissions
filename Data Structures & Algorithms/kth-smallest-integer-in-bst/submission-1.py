# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return -1
        
        res = None
        def dfs(cur):
            nonlocal res, k
            if res is not None or cur is None:
                return
            
            dfs(cur.left)
            k -= 1
            if k == 0:
                res = cur.val
                return
            dfs(cur.right)
            return
        dfs(root)
        return res


