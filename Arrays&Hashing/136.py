# Single Number - Easy
from typing import List
from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int: # Hashing
        numMap = Counter(nums)
        for (key, value) in numMap.items():
            if value == 1:
                return key
        return 0
    
    def singleNumber2(self, nums: List[int]) -> int: # XOR
        value = 0
        for num in nums:
            value ^= num
        return value
    
def main():
    test_cases = [
        [2,2,1], # 1
        [4,1,2,1,2], # 4
        [1], # 1
    ]
    solution = Solution()
    for i, nums in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input nums:", nums)
        print("Output:", solution.singleNumber2(nums))
        print()

if __name__ == "__main__":
    main()