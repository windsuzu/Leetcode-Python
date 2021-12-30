from typing import List
from collections import defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if (node_count := n) == 1:
            return [0]

        # create adjacency matrix
        adj = defaultdict(set)
        for (a, b) in edges:
            adj[a].add(b)
            adj[b].add(a)

        # find leaf nodes
        leaf_nodes = [node for node in adj if len(adj[node]) == 1]

        # cut leaf nodes until the total of nodes <= 2
        while node_count > 2:
            node_count -= len(leaf_nodes)
            next_leaf_nodes = []

            for leaf in leaf_nodes:
                parent = adj[leaf].pop()
                adj[parent].remove(leaf)

                if len(adj[parent]) == 1:
                    next_leaf_nodes.append(parent)
            leaf_nodes = next_leaf_nodes
        return leaf_nodes