# Reverse String - Easy
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            temp = s[i]
            s[i] = s[len(s) - i - 1]
            s[len(s) - i - 1] = temp
            
    def reverseString2(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        j = len(s) - 1
        for i in range(len(s) // 2):
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            j -= 1

    def reverseString3(self, s: List[str]) -> None: # Two Pointer
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

def main():
    test_cases = [
        ["h","e","l","l","o"], # ["o","l","l","e","h"]
        ["H","a","n","n","a","h"] # ["h","a","n","n","a","H"]
    ]
    solution = Solution()
    for i, s in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input s:", s)
        solution.reverseString2(s)
        print("Output:", s)
        print()

if __name__ == "__main__":
    main()