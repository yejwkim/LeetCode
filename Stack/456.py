# 132 Pattern - Medium
from typing import List
import sys

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        minimums: List[int] = []
        stack: List[int] = []
        for i in range(len(nums)):
            if i == 0:
                minimums.append(i)
            else:
                if nums[i] < nums[minimums[-1]]:
                    minimums.append(i)
                else:
                    minimums.append(minimums[-1])
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            if stack:
                if nums[minimums[stack[-1]]] < nums[i]:
                    return True
            stack.append(i)
        return False

    def find132pattern2(self, nums: List[int]) -> bool:
        stack: List[int] = []
        s3 = -sys.maxsize
        for n in nums[::-1]:
            print(n, s3, stack)
            if n < s3:
                return True
            while stack and stack[-1] < n:
                s3 = stack.pop()
            stack.append(n)
        return False

def main():
    test_cases = [
        [1,2,3,4], # false
        [3,1,4,2], # true
        [-1,3,2,0], # true
        [3,5,0,3,4], # true (SUBSEQUENCE!! 3,5,4 works)
        [2,3,5,2,3] # true (2,5,3)
    ]
    solution = Solution()
    for i, nums in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input nums:", nums)
        print("Output:", solution.find132pattern2(nums))
        print()

if __name__ == "__main__":
    main()