# Find Peak Element - Medium
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
    
def main():
    test_cases = [
        [1,2,3,1], # 2
        [1,2,1,3,5,6,4] # 5
    ]
    solution = Solution()
    for i, nums in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input nums:", nums)
        print("Output:", solution.findPeakElement(nums))
        print()

if __name__ == "__main__":
    main()