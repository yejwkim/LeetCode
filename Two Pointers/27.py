# Remove Element - Easy
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        return left
    
def main():
    test_cases = [
        ([3,2,2,3], 3), # 2
        ([0,1,2,2,3,0,4,2], 2) # 5
    ]
    solution = Solution()
    for i, (nums, val) in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input nums:", nums)
        print("Input val:", val)
        print("Output:", solution.removeElement(nums, val))
        print()

if __name__ == "__main__":
    main()