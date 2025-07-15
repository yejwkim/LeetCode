# Word Search II - Hard
from typing import List
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]: # First approach; TLE
        ROWS, COLS = len(board), len(board[0])
        res = []
        def dfs(word, idx, r, c):
            if idx == len(word):
                return True
            if not (0 <= r < ROWS and 0 <= c < COLS) or board[r][c] != word[idx]:
                return False
            tmp, board[r][c] = board[r][c], "#"
            found = dfs(word,idx+1,r+1,c) or dfs(word,idx+1,r-1,c) or dfs(word,idx+1,r,c+1) or dfs(word,idx+1,r,c-1)
            board[r][c] = tmp
            return found
        for word in words:
            found = False
            for i in range(ROWS):
                for j in range(COLS):
                    if board[i][j] == word[0] and dfs(word, 0, i, j) and not found:
                        res.append(word)
                        found = True
        return res

    def findWords2(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            node = root
            for c in w:
                node = node.children[c]
            node.word = w
        
        ROWS, COLS = len(board), len(board[0])
        res = []
        def dfs(r, c, parent):
            char = board[r][c]
            node = parent.children.get(char)
            if not node:
                return None
            if node.word:
                res.append(node.word)
                node.word = None
            board[r][c] = "#"
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r+dr, c+dc
                if (0 <= nr < ROWS and 0 <= nc < COLS) and board[nr][nc] != "#":
                    dfs(nr, nc, node)
            board[r][c] = char
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, root)
        return res