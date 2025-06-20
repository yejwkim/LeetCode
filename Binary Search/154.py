# Find Minimum in Rotated Sorted Array II - Hard
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if left != mid and nums[left] == nums[mid]:
                left += 1
            elif nums[left] <= nums[mid]:
                if nums[left] < nums[right]:
                    return nums[left]
                else:
                    left = mid + 1
            else:
                right = mid
        return nums[left]
    
def main():
    test_cases = [
        [3,4,5,1,2], # 1
        [1,3,5], # 1
        [2,2,2,0,1], # 0
        [2,2,0,2,2,2,2] # 0
    ]
    solution = Solution()
    for i, nums in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input nums:", nums)
        print("Output:", solution.findMin(nums))
        print()

if __name__ == "__main__":
    main()