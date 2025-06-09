# Minimum Add to Make Parentheses Valid - Medium
from typing import List

class Solution:
    def minAddToMakeValid(self, s: str) -> int: # Stack
        stack: List[str] = []
        res = 0
        for char in s:
            if char == "(":
                stack.append(char)
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    res += 1
        return res + len(stack)
    
    def minAddToMakeValid2(self, s: str) -> int: # One-pass
        left = right = 0
        for char in s:
            if right == 0 and char == ')':
                left += 1
            else:
                right += 1 if char == '(' else -1
        return left + right
    
def main():
    test_cases = [
        "())", # 1
        "(((", # 3
        "()))((" # 4
    ]
    solution = Solution()
    for i, s in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input s:", s)
        print("Output:", solution.minAddToMakeValid2(s))
        print()

if __name__ == "__main__":
    main()