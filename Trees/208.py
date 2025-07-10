# Implement Trie (Prefix Tree) - Medium

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if cur.children[idx] is None:
                new_node = TrieNode()
                cur.children[idx] = new_node
            cur = cur.children[idx]
        cur.isEndOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if cur.children[idx] is None:
                return False
            cur = cur.children[idx]
        return cur.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            idx = ord(char) - ord('a')
            if cur.children[idx] is None:
                return False
            cur = cur.children[idx]
        return True