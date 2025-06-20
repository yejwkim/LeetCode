# Find Minimum in Rotated Sorted Array - Medium
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[left] <= nums[mid]:
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
        [4,5,6,7,0,1,2], # 0
        [11,13,15,17], # 11
        [2,1] # 1
    ]
    solution = Solution()
    for i, nums in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input nums:", nums)
        print("Output:", solution.findMin(nums))
        print()

if __name__ == "__main__":
    main()