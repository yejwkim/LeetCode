# Find All Anagrams in a String - Medium
from typing import List

class Solution:    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        res: List[int] = []
        count = [0] * 26
        for i, char in enumerate(p):
            count[ord(char) - ord('a')] += 1
            count[ord(s[i]) - ord('a')] -= 1
        if self.isAnagram(count):
            res.append(0)
        for i in range(len(s) - len(p)):
            count[ord(s[i + len(p)]) - ord('a')] -= 1
            count[ord(s[i]) - ord('a')] += 1
            if self.isAnagram(count):
                res.append(i + 1)
        return res

    def isAnagram(self, count: List[int]) -> bool:
        for elem in count:
            if elem != 0:
                return False
        return True

    def findAnagrams2(self, s: str, p: str) -> List[int]: # Without using a new method
        if len(s) < len(p):
            return []
        res: List[int] = []
        count = [0] * 26
        for i, char in enumerate(p):
            count[ord(char) - ord('a')] += 1
            count[ord(s[i]) - ord('a')] -= 1
        diff = sum(1 for c in count if c != 0)
        if diff == 0:
            res.append(0)
        for i in range(len(s) - len(p)):
            out_idx = ord(s[i]) - ord('a')
            in_idx = ord(s[i + len(p)]) - ord('a')
            
            if count[out_idx] == 0:
                diff += 1
            count[out_idx] += 1
            if count[out_idx] == 0:
                diff -= 1
            
            if count[in_idx] == 0:
                diff += 1
            count[in_idx] -= 1
            if count[in_idx] == 0:
                diff -= 1    

            if diff == 0:
                res.append(i + 1)
        return res

def main():
    test_cases = [
        ("cbaebabacd", "abc"), # [0,6]
        ("abab", "ab"), # [0, 1, 2]
        ("baa", "aa") # [1]
    ]
    solution = Solution()
    for i, (s, p) in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input s:", s)
        print("Input p:", p)
        print("Output:", solution.findAnagrams2(s, p))
        print()

if __name__ == "__main__":
    main()