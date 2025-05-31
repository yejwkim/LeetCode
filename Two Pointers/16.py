# 3Sum Closest - Medium
from typing import List
import sys

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # closestSum = float('inf')
        closestSum = sys.maxsize
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(closestSum - target) > abs(total - target):
                    closestSum = total
                if total > target:
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    return total
        return closestSum
    
def main():
    test_cases = [
        ([-1,2,1,-4],1), # 2
        ([0,0,0], 1), # 0
        ([1,2,3,4], 8) # 8
    ]
    solution = Solution()
    for i, (nums, target) in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input nums:", nums)
        print("Input target:", target)
        print("Output:", solution.threeSumClosest(nums, target))
        print()

if __name__ == "__main__":
    main()