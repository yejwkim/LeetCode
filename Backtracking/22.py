# Generate Parentheses - Medium
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(path, open_p, close_p):
            if len(path) == 2 * n:
                res.append("".join(path))
                return
            if open_p < n:
                path.append("(")
                backtrack(path, open_p + 1, close_p)
                path.pop()
            if close_p < open_p:
                path.append(")")
                backtrack(path, open_p, close_p + 1)
                path.pop()
        backtrack([], 0, 0)
        return res