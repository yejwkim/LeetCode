# Remove Duplicates from Sorted Array - Easy
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_pos = 0
        for i in range(len(nums)):
            if nums[unique_pos] != nums[i]:
                nums[unique_pos + 1], nums[i] = nums[i], nums[unique_pos + 1]
                unique_pos += 1
        return unique_pos + 1
    
    def removeDuplicates2(self, nums: List[int]) -> int: # Better version
        unique_pos = 0
        for i in range(len(nums)):
            if nums[unique_pos] != nums[i]:
                unique_pos += 1
                nums[unique_pos] = nums[i]
        return unique_pos + 1

def main():
    test_cases = [
        [1,1,2], # 2
        [0,0,1,1,1,2,2,3,3,4] # 5
    ]
    solution = Solution()
    for i, nums in enumerate(test_cases):
        print(f"Test Case {i+1}:")
        print("Input nums:", nums)
        print("Output:", solution.removeDuplicates2(nums))
        print()

if __name__ == "__main__":
    main()