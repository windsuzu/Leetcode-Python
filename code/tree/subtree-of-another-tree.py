from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # we can reuse the code from [100. Same Tree]
        # https://leetcode.com/problems/same-tree/
        # and recursively check if node is "isSameTree".

        if not subRoot: return True
        if not root: return False
        if self.isSameTree(root, subRoot): return True
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))

    
    def isSameTree(self, p: TreeNode, q: TreeNode):
        # same idea as [100. Same Tree]
        if not p and not q: 
            return True
        if not p or not q or p.val != q.val:
            return False
        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))