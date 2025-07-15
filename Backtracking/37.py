# Sudoku Solver - Hard
from typing import List
from collections import defaultdict

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = set()
        cols = set()
        subbox = set()

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    rows.add((int(board[r][c]), r))
                    cols.add((int(board[r][c]), c))
                    subbox.add((int(board[r][c]), r//3, c//3))
        
        def backtrack(r, c):
            if r == 9:
                return True
            if c == 9:
                return backtrack(r + 1, 0) 
            if board[r][c] != ".":
                return backtrack(r, c + 1)
            for i in range(1, 10):
                if (i, r) in rows or (i, c) in cols or (i, r//3, c//3) in subbox:
                    continue
                rows.add((i, r))
                cols.add((i, c))
                subbox.add((i, r//3, c//3))
                board[r][c] = str(i)
                if backtrack(r, c + 1):
                    return True
                rows.remove((i, r))
                cols.remove((i, c))
                subbox.remove((i, r//3, c//3))
                board[r][c] = "."
            return False

        backtrack(0, 0)

    def solveSudoku2(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        subbox = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    subbox[(r//3, c//3)].add(board[r][c])
        
        def backtrack(r, c):
            if r == 9:
                return True
            if c == 9:
                return backtrack(r + 1, 0)
            if board[r][c] != ".":
                return backtrack(r, c + 1)
            for i in range(1, 10):
                chi = str(i)
                if chi in rows[r] or chi in cols[c] or chi in subbox[(r//3, c//3)]:
                    continue
                board[r][c] = chi
                rows[r].add(chi)
                cols[c].add(chi)
                subbox[(r//3, c//3)].add(chi)
                if backtrack(r, c + 1):
                    return True
                board[r][c] = "."
                rows[r].remove(chi)
                cols[c].remove(chi)
                subbox[(r//3, c//3)].remove(chi)
            return False
        backtrack(0, 0)

def main():
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    solution = Solution()
    print(f"Input board: {board}")
    solution.solveSudoku2(board)
    print(f"Output: {board}")
    print()

if __name__ == "__main__":
    main()
