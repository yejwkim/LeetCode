# Letter Combinations of a Phone Number - Medium
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phoneMap = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }
        res = []
        def backtrack(idx, path):
            if idx == len(digits):
                res.append("".join(path))
                return
            for c in phoneMap[digits[idx]]:
                path.append(c)
                backtrack(idx + 1, path)
                path.pop()
        backtrack(0, [])
        return res