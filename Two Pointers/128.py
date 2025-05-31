# Longest Consecutive Sequence - Medium
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)
        for num in numSet:
            if num - 1 not in numSet:
                length = 1
                while num + length in numSet:
                    length += 1
                longest = max(longest, length)
        return longest

def main():
    test_cases = [
        [100,4,200,1,3,2], # 4
        [0,3,7,2,5,8,4,6,0,1], # 9
        [1,0,1,2] # 3
    ]
    solution = Solution()
    for i, nums in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input nums:", nums)
        print("Output:", solution.longestConsecutive(nums))
        print()

if __name__ == "__main__":
    main()