# Sliding Window Maximum - Hard
from typing import List
import heapq
from collections import defaultdict, deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]: # Heap; O(n log k)
        heap: List[int] = []
        for i in range(k):
            heapq.heappush(heap, -nums[i])
        res = [-heap[0]]
        to_remove: dict[int, int] = defaultdict(int)
        for i in range(k, len(nums)):
            heapq.heappush(heap, -nums[i])
            to_remove[nums[i - k]] += 1
            while heap and to_remove[-heap[0]] > 0:
                to_remove[-heap[0]] -= 1
                heapq.heappop(heap)
            res.append(-heap[0])
        return res

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]: # Monotonic Deque; O(n)
        dq: deque[int] = deque()
        res = []
        for i in range(len(nums)):
            if dq and dq[0] <= i-k:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k-1:
                res.append(nums[dq[0]])     
        return res  