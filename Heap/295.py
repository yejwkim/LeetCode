# Find Median from Data Stream - Hard
import heapq

class MedianFinder:
    def __init__(self):
        self.leftHeap = [] # Max Heap
        self.rightHeap = [] # Min Heap

    def addNum(self, num: int) -> None:
        if not self.rightHeap or num >= self.rightHeap[0]:
            heapq.heappush(self.rightHeap, num)
        else:
            heapq.heappush(self.leftHeap, -num)
        if len(self.rightHeap) > len(self.leftHeap) + 1:
            heapq.heappush(self.leftHeap, -heapq.heappop(self.rightHeap))
        elif len(self.leftHeap) > len(self.rightHeap):
            heapq.heappush(self.rightHeap, -heapq.heappop(self.leftHeap))

    def findMedian(self) -> float:
        if len(self.leftHeap) == len(self.rightHeap):
            return (-self.leftHeap[0] + self.rightHeap[0]) / 2
        else:
            return self.rightHeap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()