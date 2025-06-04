# Evaluate Reverse Polish Notation - Medium
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: List[int] = []
        for elem in tokens:
            if elem not in ["+", "-", "*", "/"]:
                stack.append(int(elem))
                continue
            if elem == "+":
                stack.append(stack.pop() + stack.pop())
            elif elem == "-":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(num2 - num1)
            elif elem == "/":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(int(num2 / num1))
            elif elem == "*":
                stack.append(stack.pop() * stack.pop())
        return stack[0]

def main():
    test_cases = [
        ["2","1","+","3","*"], # 9
        ["4","13","5","/","+"], # 6
        ["10","6","9","3","+","-11","*","/","*","17","+","5","+"] # 22
    ]
    solution = Solution()
    for i, tokens in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input tokens:", tokens)
        print("Output:", solution.evalRPN(tokens))
        print()

if __name__ == "__main__":
    main()