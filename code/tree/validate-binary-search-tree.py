from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        bound = (float("-inf"), float("inf"))
        
        def dfs(node, bound):
            if not node:
                return True
            if node.val <= bound[0] or node.val >= bound[1]:
                return False
            
            return (dfs(node.left, (bound[0], node.val)) and
                    dfs(node.right, (node.val, bound[1])))

        return dfs(root, bound)