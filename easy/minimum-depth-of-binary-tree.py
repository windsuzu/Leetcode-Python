from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        current_nodes = [root]
        level = 1
        
        while current_nodes:
            temp = []
            
            for node in current_nodes:
                if not node.left and not node.right:
                    return level
                
                if node.left:
                    temp.append(node.left)
                
                if node.right:
                    temp.append(node.right)
            
            current_nodes = temp
            level += 1
        
        return level
                    
                