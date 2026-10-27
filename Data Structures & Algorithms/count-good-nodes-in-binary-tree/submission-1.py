# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class NewNode:
#     def __init__(self, TreeNode = None, max_past = -1):
#         self.val = TreeNode.val
#         self.left = TreeNode.left
#         self.right = TreeNode.right
#         if max_past == -1:
#             print('test')
#             self.max_past = TreeNode.val
#         if self.max_past < TreeNode.val:
#             self.max_past = TreeNode.val

class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        if root is None or not root:
            return 0

        def dfs(node, max_val):
            if not node:
                return 0
            if node.val >= max_val:
                res = 1
            else:
                res = 0
            new_max = max(max_val, node.val)
            res += dfs(node.left, new_max)
            res += dfs(node.right, new_max)
            return res
    
        return dfs(root, root.val)
