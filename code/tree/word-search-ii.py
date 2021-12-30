from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isEnd = True
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # the idea is to use a "Trie" to store all the words
        # and implement word search like [79. Word Search]
        # we add the word to the result when "node.isEnd" is True
        
        m, n = len(board), len(board[0])
        res, seen = set(), set()
        
        trie = Trie()
        for word in words:
            trie.addWord(word)
        
        def dfs(i, j, node, word):
            if (i < 0 or j < 0 or i == m or j == n or
                (i, j) in seen or board[i][j] not in node.children):
                return False
            
            node = node.children[board[i][j]]
            word += board[i][j]
            
            if node.isEnd:
                res.add(word)
                            
            seen.add((i, j))
            dfs(i-1, j, node, word)            
            dfs(i+1, j, node, word)
            dfs(i, j-1, node, word)
            dfs(i, j+1, node, word)
            seen.remove((i, j))
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie.root, "")
        return res