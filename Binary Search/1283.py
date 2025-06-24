# Find the Smallest Divisor Given a Threshold - Medium
from typing import List
import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            divisor = sum(math.ceil(num / mid) for num in nums)
            if divisor <= threshold:
                right = mid
            else:
                left = mid + 1
        return left
    
    def smallestDivisor2(self, nums: List[int], threshold: int) -> int: # With cache
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            total = 0
            for x in nums:
                total += (x + mid - 1) // mid
                if total > threshold:
                    break
            if total <= threshold:
                right = mid
            else:
                left = mid + 1
        return left
    
def main():
    test_cases = [
        ([1,2,5,9], 6), # 5
        ([44,22,33,11,1], 5), # 44
    ]
    solution = Solution()
    for i, (nums, threshold) in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input nums:", nums)
        print("Input threshold:", threshold)
        print("Output:", solution.smallestDivisor2(nums, threshold))
        print()

if __name__ == "__main__":
    main()