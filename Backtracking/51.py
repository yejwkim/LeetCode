# N-Queens - Hard
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        chessboard = [["."] * n for _ in range(n)]
        cols = set()
        pos_diag = set()
        neg_diag = set()
        def backtrack(r, chessboard):
            if r == n:
                res.append(["".join(row) for row in chessboard])
                return
            for c in range(n):
                if c in cols or r + c in pos_diag or r - c in neg_diag:
                    continue
                chessboard[r][c] = "Q"
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                backtrack(r + 1, chessboard)
                chessboard[r][c] = "."
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
        backtrack(0, chessboard)
        return res

def main():
    test_cases = (
        4,
        1
    )
    solution = Solution()
    for i, n in enumerate(test_cases):
        print(f"Test Case #{i+1}:")
        print(f"Input n: {n}")
        print(f"Output: {solution.solveNQueens(n)}")
        print()

if __name__ == "__main__":
    main()
