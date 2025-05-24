# Container With Most Water - Medium
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxVal = 0
        while left < right:
            maxVal = max(maxVal, min(height[left], height[right]) * (right - left))
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return maxVal

def main():
    test_cases = [
        [1,8,6,2,5,4,8,3,7], # 49
        [1,1] # 1
    ]
    solution = Solution()
    for i, height in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input height:", height)
        print("Output:", solution.maxArea(height))
        print()

if __name__ == "__main__":
    main()