# Word Search - Medium
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool: # First approach; Got TLE
        num_row, num_col = len(board), len(board[0])
        used = [[False] * num_col for _ in range(num_row)]
        self.found = False
        def backtrack(idx, row, col, path):
            if "".join(path) == word:
                self.found = True
                return
            for i in range(num_row):
                for j in range(num_col):
                    if board[i][j] != word[idx] or used[i][j]:
                        continue
                    if idx > 0 and (abs(row - i) != 1 or j != col) and (i != row or abs(col - j) != 1):
                        continue
                    used[i][j] = True
                    path.append(board[i][j])
                    backtrack(idx + 1, i, j, path)
                    used[i][j] = False
                    path.pop()
        backtrack(0, 0, 0, [])
        return self.found

    def exist2(self, board: List[List[str]], word: str) -> bool:
        num_row, num_col = len(board), len(board[0])
        def dfs(idx, row, col):
            if idx == len(word):
                return True
            if not (0 <= row < num_row and 0 <= col < num_col) or board[row][col] != word[idx]:
                return False
            tmp, board[row][col] = board[row][col], "#"
            for dr, dc in (0, 1), (0, -1), (1, 0), (-1, 0):
                if dfs(idx + 1, row + dr, col + dc):
                    return True
            board[row][col] = tmp
            return False
            
        for i in range(num_row):
            for j in range(num_col):
                if board[i][j] == word[0] and dfs(0, i, j):
                    return True
        return False

def main():
    test_cases = (
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"),
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"),
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")
    )
    solution = Solution()
    for i, (board, word) in enumerate(test_cases):
        print(f"Test Case #{i+1}:")
        print(f"Input board: {board}")
        print(f"Input word: {word}")
        print(f"Output: {solution.exist2(board, word)}")
        print()

if __name__ == "__main__":
    main()
