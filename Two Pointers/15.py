# 3Sum - Medium
from typing import List
from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: # O(n^2)
        # if len(nums) < 3:
        #     return []
        nums.sort()
        solutionSet = set()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[left] + nums[right]
                if total == target:
                    solutionSet.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # while left < right and nums[right] == nums[right + 1]:
                    #     right -= 1
                elif total > target:
                    right -= 1
                else:
                    left += 1
        return [list(triplet) for triplet in solutionSet]

    def threeSum2(self, nums: List[int]) -> List[List[int]]: # Shared Solution
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res

def main():
    test_cases = [
        [-1,0,1,2,-1,-4], # [[-1,-1,2],[-1,0,1]]
        [0,1,1], # []
        [0,0,0], # [[0,0,0]]
        [-2,0,1,1,2] # [[-2,0,2],[-2,1,1]]
    ]
    solution = Solution()
    for i, nums in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input nums:", nums)
        print("Output:", solution.threeSum(nums))
        print()

if __name__ == "__main__":
    main()