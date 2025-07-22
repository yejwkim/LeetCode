# Sliding Window Median - Hard
from typing import List
import heapq
from collections import defaultdict

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        low: List[int] = [] # Max Heap
        high: List[int] = [] # Min Heap
        res: List[float]
        for i in range(k):
            if len(low) == len(high):
                heapq.heappush(high, -heapq.heappushpop(low, -nums[i]))
            else:
                heapq.heappush(low, -heapq.heappushpop(high, nums[i]))
        res = [high[0]] if k & 1 else [(high[0] - low[0]) / 2]
        to_remove: dict[int, int] = defaultdict(int)
        for i in range(k, len(nums)):
            heapq.heappush(high, -heapq.heappushpop(low, -nums[i]))
            out_num = nums[i - k]
            to_remove[out_num] += 1
            if out_num < high[0]:
                heapq.heappush(low, -heapq.heappop(high))
            while to_remove[high[0]]:
                to_remove[high[0]] -= 1
                heapq.heappop(high)
            while low and to_remove[-low[0]]:
                to_remove[-low[0]] -= 1
                heapq.heappop(low)
            if k % 2:
                res.append(high[0])
            else:
                res.append((high[0] - low[0]) / 2)
        return res

def main():
    solution = Solution()
    test_cases = [
        ([1,3,-1,-3,5,3,6,7], 3), # [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
        ([1,2,3,4,2,3,1,4,2], 3), # [2.0, 3.0, 3.0, 3.0, 2.0, 3.0, 2.0]
        ([7,8,7,7,4], 4), # [7.0, 7.0]
        ([7,0,3,9,9,9,1,7,2,3], 6) # [8.0, 6.0, 8.0, 8.0, 5.0]
    ]
    for i, (nums, k) in enumerate(test_cases):
        print(f"Test Case {i+1}:")
        print(f"Input nums: {nums}")
        print(f"Input k: {k}")
        print(f"Output: {solution.medianSlidingWindow(nums, k)}")
        print()

if __name__ == "__main__":
    main()