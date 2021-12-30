# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # we can have 3 conditions when we meet each node:
        # 1. if p, q > node, LCA must be on the right
        # 2. if p, q < node, LCA must be on the left
        # 3. if p, q split into 2 branches, or any one equal to the node,
        #    LCA must be the node
        
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
        
        