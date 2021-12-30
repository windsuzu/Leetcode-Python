from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return
        res = []

        def dfs(node=root, path=[root.val]):
            if not (node.left or node.right) and sum(path) == targetSum:
                res.append(path.copy())

            if node.left:
                dfs(node.left, path + [node.left.val])

            if node.right:
                dfs(node.right, path + [node.right.val])

        dfs()
        return res
