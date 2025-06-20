# Search in Rotated Sorted Array - Medium
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                if target >= nums[left] and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target >= nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

def main():
    test_cases = [
        ([4,5,6,7,0,1,2], 0), # 4
        ([4,5,6,7,0,1,2], 3), # -1
        ([1], 0), # -1
        ([5,1,3], 1) # 1
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