from typing import List, Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevelsDFS(self, root: Optional[TreeNode]) -> List[float]:
        # the idea is to use a "dict" to store the elements in the same level
        # and use a variable "depth" to update the max depth
        
        res = defaultdict(list)
        depth = [0]
        
        def dfs(node, level):
            if node:
                res[level].append(node.val)
                depth[0] = max(depth[0], level)

                dfs(node.left, level+1)
                dfs(node.right, level+1)
        
        dfs(root, 0)
        return [sum(res[i])/len(res[i]) for i in range(depth[0] + 1)]
    
    
    def averageOfLevelsBFS(self, root: Optional[TreeNode]) -> List[float]:
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