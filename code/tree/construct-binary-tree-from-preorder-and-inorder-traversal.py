from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 1. the first element of the "preorder" must be the root
        # 2. the root element can be used to seperate left/right in the "inorder"
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(root.val)
        
        # mid will also indicate the size of left tree,
        # so we can use mid to split the left/right in the "preorder" 
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root