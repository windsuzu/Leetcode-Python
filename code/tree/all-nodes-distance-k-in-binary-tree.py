from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # use a hashtable to store the direction from node to its parent.
        q, ht = [root], {}
        while q:
            tmp = []
            for node in q:
                if node.left:
                    ht[node.left] = node
                    tmp.append(node.left)
                if node.right:
                    ht[node.right] = node
                    tmp.append(node.right)
            q = tmp

        # run BFS from the target node (as the root) in 3 directions (left, right, parent)
        res, q, visited = [], [(target, 0)], set([target])
        while q:
            tmp = []
            for (node, distance) in q:
                if distance == k:
                    res.append(node.val)
                    continue  # no need to search further

                if ht.get(node) and ht[node] not in visited:
                    visited.add(ht[node])
                    tmp.append((ht[node], distance + 1))

                if node.left and node.left not in visited:
                    visited.add(node.left)
                    tmp.append((node.left, distance + 1))

                if node.right and node.right not in visited:
                    visited.add(node.right)
                    tmp.append((node.right, distance + 1))
            q = tmp
        return res