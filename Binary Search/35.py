# Search Insert Position - Easy
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            index = (left + right) // 2
            if nums[index] > target:
                right = index - 1
            elif nums[index] < target:
                left = index + 1
            else:
                return index
        return left

def main():
    test_cases = [
        ([1,3,5,6], 5), # 2
        ([1,3,5,6], 2), # 1
        ([1,3,5,6], 7) # 4
    ]
    solution = Solution()
    for i, (nums, target) in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input nums:", nums)
        print("Input target:", target)
        print("Output:", solution.searchInsert(nums, target))
        print()

if __name__ == "__main__":
    main()