# Top K Frequent Elements - Medium
from typing import List
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: # Hashmap + Heap
        numMap = Counter(nums)
        heap: List[tuple[int, int]] = []
        for num, freq in numMap.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            else:
                heapq.heappushpop(heap, (freq, num))
        return [num for _, num in heap]
    
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]: # Bucket Sort
        freq = Counter(nums)
        buckets: List[List[int]] = [[] for _ in range(len(nums)+1)]
        for num, f in freq.items():
            buckets[f].append(num)
        res = []
        for f in range(len(buckets)-1, 0, -1):
            for num in buckets[f]:
                res.append(num)
                if len(res) == k:
                    return res
        return []