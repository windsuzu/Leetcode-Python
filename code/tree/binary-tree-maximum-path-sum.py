from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # the idea is to use DFS and update 2 vars on each node
        # 1. maximum with split e.g. [1,2,3] -> 6
        # 2. maximum without split e.g. [1,2,3] -> 4
        # and be aware of negative values
        self.res = root.val
        
        def dfs(node):
            if not node:
                return 0
            
            left_val = max(0, dfs(node.left))
            right_val = max(0, dfs(node.right))
            
            self.res = max(self.res, node.val + left_val + right_val)
            
            return node.val + max(left_val, right_val)
        
        dfs(root)
        return self.res