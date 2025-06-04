# Shortest Unsorted Continuous Subarray - Medium
from typing import List
import sys

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack: List[int] = []
        left, right = len(nums), 0
        for i in range(len(nums)):
            while stack and nums[i] < nums[stack[-1]]:
                left = min(left, stack.pop())
            stack.append(i)
        stack.clear()
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] > nums[stack[-1]]:
                right = max(right, stack.pop())
            stack.append(i)
        if right <= left:
            return 0
        return right - left + 1

    def findUnsortedSubarray2(self, nums: List[int]) -> int: # Without stack
        n, left, right, minVal, maxVal = len(nums), -1, -2, nums[-1], nums[0]
        for i in range(n):
            maxVal = max(maxVal, nums[i])
            minVal = min(minVal, nums[n - 1 - i])
            if nums[i] < maxVal:
                right = i
            if nums[n - 1 - i] > minVal:
                left = n - 1 - i
        return right - left + 1

def main():
    test_cases = [
        [2,6,4,8,10,9,15], # 5
        [1,2,3,4], # 0
        [1], # 0
        [1,7,3,4,6], # 4
        [15,1,2,3], # 4
        [1,4,3,2,5], # 3
        [1,3,2,3,3], # 2
        [2,3,3,2,4] # 3
    ]
    solution = Solution()
    for i, nums in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input nums:", nums)
        print("Output:", solution.findUnsortedSubarray2(nums))
        print()

if __name__ == "__main__":
    main()