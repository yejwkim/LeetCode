# Score of Parentheses - Medium
from typing import List

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack: List[str] = []
        for char in s:
            if char == "(":
                stack.append(char)
            else:
                if stack[-1] == "(":
                    stack.pop()
                    stack.append('1')
                else:
                    score = 0
                    while stack[-1] != "(":
                        score += int(stack.pop())
                    stack.pop()
                    stack.append(str(2 * score))
        return sum(map(int, stack))

    def scoreOfParentheses2(self, S: str) -> int:
        res = l = 0
        for a, b in zip(S, S[1:]):
            if a + b == '()': res += 2 ** l
            l += 1 if a == '(' else -1
        return res

    def scoreOfParentheses3(self, S: str) -> int:
        stack: List[int] = []
        cur = 0
        for i in S:
            print(stack, cur)
            if i == '(':
                stack.append(cur)
                cur = 0
            else:
                cur += stack.pop() + max(cur, 1)
        return cur

def main():
    test_cases = [
        "()", # 1
        "(())", # 2
        "()()", # 2
        "(()(()))" # 6; (1 + 1 * 2) * 2
    ]
    solution = Solution()
    for i, s in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input nums:", s)
        print("Output:", solution.scoreOfParentheses3(s))
        print()

if __name__ == "__main__":
    main()