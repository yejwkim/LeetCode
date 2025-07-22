# Smallest Range Covering Elements from K Lists - Hard

from typing import List
import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap: List[tuple[int, int, int]] = []
        cur_max = float('-inf')
        for i, num in enumerate(nums):
            heapq.heappush(heap, (num[0], i, 0))
            if (num[0] > cur_max):
                cur_max = num[0]
        min_range = cur_max - heap[0][0]
        res = [heap[0][0], int(cur_max)]
        while True:
            _, k, idx = heapq.heappop(heap)
            if idx + 1 == len(nums[k]):
                break
            heapq.heappush(heap, (nums[k][idx + 1], k, idx + 1))
            if nums[k][idx + 1] > cur_max:
                cur_max = nums[k][idx + 1]
            if cur_max - heap[0][0] < min_range:
                min_range = cur_max - heap[0][0]
                res = [heap[0][0], int(cur_max)]
        return res