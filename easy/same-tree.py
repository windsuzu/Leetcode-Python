from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        current_nodes = [(p, q)]
        
        while current_nodes:
            temp = []
            for p, q in current_nodes:
                if (p and not q) or (not p and q):
                    return False
                elif p and q and p.val != q.val:
                    return False
                
                if p and q:
                    temp.append((p.left, q.left))
                    temp.append((p.right, q.right))
            
            current_nodes = temp
            
        return True