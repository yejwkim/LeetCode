# Restore IP Addresses - Medium
from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def backtrack(start, path):
            if start == len(s):
                if len(path) == 4:
                    res.append(".".join(path))
                return
            if int(path[-1]) != 0 and int(path[-1] + s[start]) <= 255:
                tmp, path[-1] = path[-1], path[-1] + s[start]
                backtrack(start + 1, path)
                path[-1] = tmp
            if len(path) < 4:
                path.append(s[start])
                backtrack(start + 1, path)
                path.pop()
        backtrack(1, [s[0]])
        return res

    def restoreIpAddresses2(self, s: str) -> List[str]:
        res: List[str] = []
        def backtrack(start: int, path: List[str]):
            remaining_chars = len(s) - start
            segments_left = 4 - len(path)
            if remaining_chars < segments_left or remaining_chars > 3 * segments_left:
                return
            if start == len(s) and len(path) == 4:
                res.append(".".join(path))
                return
            for length in range(1, 4):
                if start + length > len(s):
                    break
                segment = s[start : start + length]
                if segment[0] == "0" and length > 1:
                    continue
                val = int(segment)
                if val > 255:
                    continue
                path.append(segment)
                backtrack(start + length, path)
                path.pop()
        backtrack(0, [])
        return res
