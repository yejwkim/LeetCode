# Search in Rotated Sorted Array II - Medium
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[left]:
                left += 1
            elif nums[mid] > nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
    
def main():
    test_cases = [
        ([2,5,6,0,0,1,2], 0), # true
        ([2,5,6,0,0,1,2], 3), # false
        ([1,0,1,1,1], 0), # true
        ([1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1], 2) # true
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