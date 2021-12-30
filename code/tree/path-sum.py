from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSumDFS(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: 
            return False
        if not root.left and not root.right and targetSum == root.val: 
            return True
        return (self.hasPathSumDFS(root.left, targetSum - root.val) or 
                self.hasPathSumDFS(root.right, targetSum - root.val))
        
        
    def hasPathSumBFS(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        nodes = [(root, root.val)]
        
        while nodes:
            temp = []
            for node, node_val in nodes:
                if node.left:
                    temp.append((node.left, node_val + node.left.val))
                if node.right:
                    temp.append((node.right, node_val + node.right.val))
                if not node.left and not node.right and node_val == targetSum:
                    return True
                    
            nodes = temp
        
        return False