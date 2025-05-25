# Remove Duplicates from Sorted Array II - Medium
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 2
        for fast in range(2, len(nums)):
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1
        return slow
    
def main():
    test_cases = [
        [1,1,1,2,2,3], # 5; [1,1,2,2,3,_]
        [0,0,1,1,1,1,2,3,3] # 7; [0,0,1,1,2,3,3,_,_]
    ]
    solution = Solution()
    for i, nums in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input nums:", nums)
        print("Output:", solution.removeDuplicates(nums))
        print()

if __name__ == "__main__":
    main()