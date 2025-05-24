# Move Zeroes - Easy
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None: # O(n^2)
        """
        Do not return anything, modify nums in-place instead.
        """
        slow, fast = 0, 1
        while slow < len(nums):
            if nums[slow] == 0:
                while fast < len(nums) and nums[fast] == 0:
                    fast += 1
                if fast < len(nums):
                    nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
                fast = slow + 1
            else:
                slow += 1
                fast = slow + 1

    def moveZeroes2(self, nums: List[int]) -> None: # O(n)
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero_pos], nums[i] = nums[i], nums[zero_pos]
                zero_pos += 1

def main():
    test_cases = [
        [0,1,0,3,12], # [1,3,12,0,0]
        [0] # [0]
    ]
    solution = Solution()
    for i, nums in enumerate(test_cases):
        print(f"Test Case {i+1}:")
        print("Input nums:", nums)
        solution.moveZeroes(nums)
        print("Output:", nums)
        print()

if __name__ == "__main__":
    main()