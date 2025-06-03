# Baseball Game - Easy
from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack: List[int] = []
        for operation in operations:
            if operation == "D":
                stack.append(stack[-1] * 2)
            elif operation == "C":
                stack.pop()
            elif operation == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(operation))
        return sum(stack)
    
def main():
    test_cases = [
        ["5","2","C","D","+"], # 30
        ["5","-2","4","C","D","9","+","+"], # 27
        ["1","C"] # 0
    ]
    solution = Solution()
    for i, operations in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input operations:", operations)
        print("Output:", solution.calPoints(operations))
        print()

if __name__ == "__main__":
    main()