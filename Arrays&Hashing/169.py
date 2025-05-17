# Majority Element - Easy
from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numMap = Counter(nums)
        maxValue = numMap[nums[0]]
        maxElem = nums[0]
        for key, value in numMap.items():
            if value > maxValue:
                maxValue = value
                maxElem = key
        return maxElem

    def majorityElement2(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        n = len(nums)
        return nums[n//2]

    def majorityElement3(self, nums: List[int]) -> int: # Moore Voting Algorithm
        count = 0
        candidate = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate

def main():
    test_cases = [
        [3,2,3], # 3
        [2,2,1,1,1,2,2], # 2
        [6,5,5] # 5
    ]
    solution = Solution()
    for i, nums in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input nums1:", nums)
        print("Output:", solution.majorityElement3(nums))
        print()

if __name__ == "__main__":
    main()