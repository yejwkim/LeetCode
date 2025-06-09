# Minimum Insertions to Balance a Parentheses String - Medium
from typing import List

class Solution:
    def minInsertions(self, s: str) -> int: # Stack
        stack: List[int] = []
        ans = 0
        for char in s:
            if char == "(":
                if not stack or stack[-1] == 2:
                    stack.append(2)
                else:
                    stack.pop()
                    stack.append(2)
                    ans += 1
            else:
                if not stack:
                    stack.append(1)
                    ans += 1
                elif stack[-1] == 2:
                    stack.pop()
                    stack.append(1)
                elif stack[-1] == 1:
                    stack.pop()
        while stack:
            ans += stack.pop()
        return ans
    
    def minInsertions2(self, s: str) -> int: # One Pass
        res = right = 0
        for c in s:
            if c == '(':
                if right % 2:
                    right -= 1
                    res += 1
                right += 2
            if c == ')':
                right -= 1
                if right < 0:
                    right += 2
                    res += 1
        return right + res
    
def main():
    test_cases = [
        "(()))", # 1
        "())", # 0
        "))())(", # 3
        "(()))(()))()())))", # 4
        "((())))))", # 0
        "(((()(()((())))(((()())))()())))(((()(()()((()()))" # 31
    ]
    solution = Solution()
    for i, s in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input s:", s)
        print("Output:", solution.minInsertions(s))
        print()

if __name__ == "__main__":
    main()