# Minimum Size Subarray Sum - Medium
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = len(nums) + 1
        total = 0
        slow = 0
        for fast, elem in enumerate(nums):
            total += elem
            while total >= target:
                minLength = min(minLength, fast - slow + 1)
                total -= nums[slow]
                slow += 1
        return minLength if minLength <= len(nums) else 0
    
def main():
    test_cases = [
        (7, [2,3,1,2,4,3]), # 2
        (4, [1,4,4]), # 1
        (11, [1,1,1,1,1,1,1,1]), # 0
        (11, [1,2,3,4,5]), # 3
        (3, [1,1,1]) # 3
    ]
    solution = Solution()
    for i, (target, nums) in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input target:", target)
        print("Input nums:", nums)
        print("Output:", solution.minSubArrayLen(target, nums))
        print()

if __name__ == "__main__":
    main()