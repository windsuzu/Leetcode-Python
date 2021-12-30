
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        # the idea is to use a hashtable to maintain nodes already copied
        
        clones = {}
        
        def dfs(node):
            if node in clones:
                return clones[node]
            
            copy = Node(node.val)
            clones[node] = copy
            copy.neighbors += [dfs(neighbor) for neighbor in node.neighbors]
            return copy
        
        return dfs(node) if node else None
        