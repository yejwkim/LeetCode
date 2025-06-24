# Koko Eating Bananas - Medium
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            hours = sum((pile + mid - 1) // mid for pile in piles)
            if hours > h:
                left = mid + 1
            else:
                right = mid
        return left

def main():
    test_cases = [
        ([3,6,7,11], 8), # 4
        ([30,11,23,4,20], 5), # 30
        ([30,11,23,4,20], 6) # 23
    ]
    solution = Solution()
    for i, (piles, h) in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input piles:", piles)
        print("Input h:", h)
        print("Output:", solution.minEatingSpeed(piles, h))
        print()

if __name__ == "__main__":
    main()