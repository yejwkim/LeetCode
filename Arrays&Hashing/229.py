# Majority Element II - Medium
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for elem in nums:
            if elem == candidate1:
                count1 += 1
            elif elem == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = elem, 1
            elif count2 == 0:
                candidate2, count2 = elem, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [n for n in (candidate1, candidate2) if nums.count(n) > len(nums) // 3]
    
def main():
    test_cases = [
        [3,2,3], # [3]
        [1], # [1]
        [1, 2] # [1,2]
    ]
    solution = Solution()
    for i, nums in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input nums1:", nums)
        print("Output:", solution.majorityElement(nums))
        print()

if __name__ == "__main__":
    main()