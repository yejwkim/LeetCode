# Kth Largest Element in an Array - Medium
from typing import List
import heapq, random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int: # Heap
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]
    
    def findKthLargest2(self, nums: List[int], k: int) -> int: # Quickselect
        target = len(nums) - k
        def partition(left: int, right: int, pivot_index: int) -> int:
            pivot_value = nums[pivot_index]
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            store = left
            for i in range(left, right):
                if nums[i] < pivot_value:
                    nums[store], nums[i] = nums[i], nums[store]
                    store += 1
            nums[store], nums[right] = nums[right], nums[store]
            return store

        def quickselect(left: int, right: int) -> int:
            if left == right:
                return nums[left]
            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)
            if pivot_index == target:
                return nums[pivot_index]
            elif pivot_index < target:
                return quickselect(pivot_index + 1, right)
            else:
                return quickselect(left, pivot_index - 1)

        return quickselect(0, len(nums) - 1)