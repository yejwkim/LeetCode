# Binary Search - Easy
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            index = int((left + right) / 2)
            if nums[index] > target:
                right = index - 1
            elif nums[index] < target:
                left = index + 1
            else:
                return index
        return -1
    
def main():
    test_cases = [
        ([-1,0,3,5,9,12], 9), # 4
        ([-1,0,3,5,9,12], 2), # -1
        ([1,2,2,3,4,6,7], 2)
    ]
    solution = Solution()
    for i, (nums, target) in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input nums:", nums)
        print("Input target:", target)
        print("Output:", solution.search(nums, target))
        print()

if __name__ == "__main__":
    main()