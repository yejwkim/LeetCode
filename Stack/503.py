# Next Greater Element II - Medium
from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]: # Next Greater Element -> Decreasing Monotonic Stack
        res: List[int] = [-1] * len(nums)
        stack: List[int] = []
        for i in range(len(nums) * 2):
            moduloIndex = i % len(nums)
            while stack and nums[moduloIndex] > nums[stack[-1]]:
                res[stack.pop()] = nums[moduloIndex]
            if i < len(nums):
                stack.append(moduloIndex)
        return res

def main():
    test_cases = [
       [1,2,1], # [2,-1,2]
       [1,2,3,4,3], # [2,3,4,-1,4]
       [1,5,3,4,3], # [5,-1,4,5,5]
       [1,5,3,2,1], # [5,-1,5,5,5]
       [1,1,1,1,1], # [-1,-1,-1,-1,-1]
       [1,2,3,2,1] # [2,3,-1,3,2]
    ]
    solution = Solution()
    for i, nums in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input nums:", nums)
        print("Output:", solution.nextGreaterElements(nums))
        print()

if __name__ == "__main__":
    main()