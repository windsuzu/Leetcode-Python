from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        current_nodes = [root]
        ans = []
        
        while len(current_nodes) > 0:
            tmp = 0
            tmp_nodes = []

            for node in current_nodes:
                tmp += node.val

                if node.left:
                    tmp_nodes.append(node.left)
                if node.right:
                    tmp_nodes.append(node.right)

            ans.append(tmp/len(current_nodes))
            current_nodes = tmp_nodes
        
        return ans