# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        res = []
        def dfs(node):
            if not node:
                res.append("null")
                return
            
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return ",".join(map(str, res))

    def deserialize(self, data):
        inp = data.split(",")
        self.index = 0
        
        def dfs():
            if inp[self.index] == "null":
                self.index += 1
                return None
            
            node = TreeNode(inp[self.index])
            self.index += 1
            node.left, node.right = dfs(), dfs()
            return node
        
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))