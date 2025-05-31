# 4Sum - Medium
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res: List[List[int]] = []
        nums.sort()
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, len(nums) - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total > target:
                        right -= 1
                    else:
                        left += 1
        return res
    
def main():
    test_cases = [
        ([1,0,-1,0,-2,2],0), # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
        ([2,2,2,2,2],8), # [[2,2,2,2]]
    ]
    solution = Solution()
    for i, (nums, target) in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input nums:", nums)
        print("Input target:", target)
        print("Output:", solution.fourSum(nums, target))
        print()

if __name__ == "__main__":
    main()