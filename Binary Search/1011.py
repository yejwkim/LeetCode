# Capacity To Ship Packages Within D Days - Medium
from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            cur_days = 0
            cur_weight = 0
            for weight in weights:
                if cur_weight + weight > mid:
                    cur_days += 1
                    cur_weight = 0
                cur_weight += weight
            cur_days += 1
            if cur_days <= days:
                right = mid
            else:
                left = mid + 1
        return left
        
def main():
    test_cases = [
        ([1,2,3,4,5,6,7,8,9,10], 5), # 15
        ([3,2,2,4,1,4], 3), # 6
        ([1,2,3,1,1], 4) # 3
    ]
    solution = Solution()
    for i, (weights, days) in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input weights:", weights)
        print("Input days:", days)
        print("Output:", solution.shipWithinDays(weights, days))
        print()

if __name__ == "__main__":
    main()