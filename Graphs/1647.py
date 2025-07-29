# Minimum Deletions to Make Character Frequencies Unique - Medium
from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        strMap = Counter(s)
        res = 0
        used = set()
        for freq in strMap.values():
            while freq > 0 and freq in used:
                freq -= 1
                res += 1
            used.add(freq)
        return res