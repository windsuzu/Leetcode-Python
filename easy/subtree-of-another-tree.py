from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isIdentical(root, subRoot):
            
            if not root and not subRoot:
                return True
            
            elif root and subRoot:
                return root.val == subRoot.val \
                        and isIdentical(root.left, subRoot.left) \
                        and isIdentical(root.right, subRoot.right)
            
            else:
                return False
        
        
        return (root and subRoot) and (isIdentical(root, subRoot) \
                or self.isSubtree(root.left, subRoot) \
                    or self.isSubtree(root.right, subRoot))