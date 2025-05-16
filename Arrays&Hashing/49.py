# Group Anagrams - Medium
from typing import List
from collections import defaultdict

class Solution1: # Too complex
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res: List[List[str]] = []
        while len(strs) != 0:
            if len(strs) == 1:
                res.append([strs.pop()])
                break
            first = strs.pop(0)
            cur = [first]
            i = 0
            while i < len(strs):
                if self.isAnagram(first, strs[i]):
                    cur.append(strs.pop(i))
                else:
                    i += 1
            res.append(cur)
        return res
    
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        for c in t:
            count[ord(c) - ord('a')] -= 1
        for val in count:
            if val != 0:
                return False
        return True

class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: # Hashmap O(n * k log k)
        anagram_map: dict[str, List[str]] = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        return list(anagram_map.values())

class Solution3:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: # Hashtable
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())

def main():
    test_cases = [
        ["eat","tea","tan","ate","nat","bat"], # [["bat"],["nat","tan"],["ate","eat","tea"]]
        [""], # [[""]]
        ["a"] # [["a"]]
    ]
    solution = Solution2()
    for i, strs in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input strs:", strs)
        print("Output:", solution.groupAnagrams(strs))
        print()
        
if __name__ == "__main__":
    main()