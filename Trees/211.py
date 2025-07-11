# Design Add and Search Words Data Structure - Medium

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.isEndOfWord = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if node is None:
                return False
            if i == len(word):
                return node.isEndOfWord
            char = word[i]
            if char == '.':
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                return dfs(node.children.get(char), i + 1)
        return dfs(self.root, 0)
