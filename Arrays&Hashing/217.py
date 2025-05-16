# Contains Duplicate - Easy
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool: # Hashmap
        numMap = {}
        for i, elem in enumerate(nums):
            if elem in numMap:
                return True
            numMap[elem] = i
        return False
    
    def containsDuplicate2(self, nums: List[int]) -> bool: # Hashset
        numSet = set()
        for elem in nums:
            if elem in numSet:
                return True
            numSet.add(elem)
        return False
    
def main():
    test_cases = [
        [1,2,3,1], # true
        [1,2,3,4], # false
        [1,1,1,3,3,4,3,2,4,2] # true
    ]
    solution = Solution()
    for i, nums in enumerate(test_cases):
        result = solution.containsDuplicate2(nums)
        print(f"Test Case {i+1}:")
        print("Input nums:", nums)
        print("Output:", result)
        print()

if __name__ == "__main__":
    main()