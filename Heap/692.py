# Top K Frequent Words - Medium
from collections import Counter
from typing import List
import heapq

class WordFreq:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word
    
    def __eq__(self, other):
        if not isinstance(other, WordFreq):
            return NotImplemented
        return self.freq == other.freq and self.word == other.word

    def __lt__(self, other):
        if not isinstance(other, WordFreq):
            return NotImplemented
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq
    
    def __str__(self):
        return "(" + str(self.freq) + ", " + self.word + ")"

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordMap = Counter(words)
        heap: List[WordFreq] = []
        for word, freq in wordMap.items():
            if len(heap) < k:
                heapq.heappush(heap, WordFreq(freq, word))
            else:
                heapq.heappushpop(heap, WordFreq(freq, word))
        res = []
        for elem in heap:
            print(elem.freq, elem.word)
        while heap:
            res.append(heapq.heappop(heap).word)
        return res[::-1]