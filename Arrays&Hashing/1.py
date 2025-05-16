# Two Sum
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: # O(n^2)
        for i, elem in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if elem + nums[j] == target:
                    return [i, j]
        return []
    
    def twoSum2(self, nums: List[int], target: int) -> List[int]: # Two-pass Hash Table; O(n)
        numMap: dict[int, int] = {}
        for i, elem in enumerate(nums):
            numMap[elem] = i
        for i, elem in enumerate(nums):
            complement = target - elem
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]
        return []
    
    def twoSum3(self, nums: List[int], target: int) -> List[int]: # One-pass Hash Table
        numMap: dict[int, int] = {}
        for i, elem in enumerate(nums):
            complement = target - elem
            if complement in numMap:
                return [numMap[complement], i]
            numMap[elem] = i
        return []
    
def main():
    test_cases = [
        ([2, 7, 11, 15], 9), # [0, 1]
        ([3, 2, 4], 6), # [1, 2]
        ([3, 3], 6) # [0, 1]
    ]
    solution = Solution()
    for i, (nums, target) in enumerate(test_cases):
        result = solution.twoSum3(nums, target)
        print(f"Test Case {i+1}:")
        print("Input nums", nums)
        print("Input target", target)
        print("Output:", result)
        print()

if __name__ == "__main__":
    main()