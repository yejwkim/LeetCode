# Remove Duplicate Letters - Medium
from typing import List

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence: dict[str, int] = {char: i for i, char in enumerate(s)}
        stack: List[str] = []
        for i, char in enumerate(s):
            if char in stack:
                continue
            while stack and stack[-1] > char and i < last_occurrence[stack[-1]]:
                stack.pop()
            stack.append(char)
        return ''.join(stack)
    
def main():
    test_cases = [
        "bcabc", # "abc"
        "cbacdcbc" # "acdb"
    ]
    solution = Solution()
    for i, s in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input s:", s)
        print("Output:", solution.removeDuplicateLetters(s))
        print()

if __name__ == "__main__":
    main()
