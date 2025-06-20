# Remove Invalid Parentheses - Hard (Save it for later; Need to know DFS, BFS, Backtracking)
from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        stack: List[str] = []
        r_remove = 0
        for char in s:
            if char == ")":
                if not stack:
                    r_remove += 1
                else:
                    stack.pop()
            elif char == "(":
                stack.append(char)
            print(stack)
        l_remove = len(stack)
        print(l_remove, r_remove)
        return []
    
def main():
    test_cases = [
        "()())()", # ["(())()","()()()"]
        "(a)())()", # ["(a())()","(a)()()"]
        "(()", # ["()"]
        ")(" # [""]
    ]
    solution = Solution()
    for i, s in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input k:", s)
        print("Output:", solution.removeInvalidParentheses(s))
        print()

if __name__ == "__main__":
    main()