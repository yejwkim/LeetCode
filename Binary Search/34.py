# Find First and Last Position of Element in Sorted Array - Medium
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        start, end = -1, -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                start = mid
                right = mid - 1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                end = mid
                left = mid + 1
        return [start, end]
        
def main():
    test_cases = [
        ([5,7,7,8,8,10], 8), # [3,4]
        ([5,7,7,8,8,10], 6), # [-1,-1]
        ([5,7,7,8,8,10], 10), # [5,5]
        ([], 0) # [-1,-1]
    ]
    solution = Solution()
    for i, (nums, target) in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input nums:", nums)
        print("Input target:", target)
        print("Output:", solution.searchRange(nums, target))
        print()

if __name__ == "__main__":
    main()