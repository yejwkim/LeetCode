# Minimum Remove to Make Valid Parentheses - Medium
from typing import List

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = list(s)
        stack: List[int] = []
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if stack:
                    stack.pop()
                else:
                    res[i] = ""
        while stack:
            res[stack.pop()] = ""
        return "".join(res)
    
    def minRemoveToMakeValid2(self, s: str) -> str: # In-place solution
        openP = 0
        closeP = 0
        for ch in s:
            if ch == ")":
                if not openP:
                    closeP += 1
                else:
                    openP -= 1
            elif ch == "(":
                openP += 1
            else:
                continue
        s = s.replace(")", "", closeP)
        s = s[::-1].replace("(", "", openP)
        s = s[::-1]
        return s
    
def main():
    test_cases = [
        "lee(t(c)o)de)", # "lee(t(c)o)de"
        "a)b(c)d", # "ab(c)d"
        "))((" # ""
    ]
    solution = Solution()
    for i, s in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input s:", s)
        print("Output:", solution.minRemoveToMakeValid(s))
        print()

if __name__ == "__main__":
    main()