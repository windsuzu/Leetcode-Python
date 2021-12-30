class TrieNode():
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            for i in range(index, len(word)):
                if (c := word[i]) != ".":
                    if c not in node.children:
                        return False
                    node = node.children[c]
                else:
                    for child in node.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
            return node.isEnd
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)