# Uncommon Words from Two Sentences - Easy
from typing import List
from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        candidate = list(set(s1.split()) ^ set(s2.split()))
        wordMap1, wordMap2 = Counter(s1.split()), Counter(s2.split())
        res = []
        for word in candidate:
            if (wordMap1[word] <= 1 and wordMap2[word] <= 1):
                res.append(word)
        return res
    
    def uncommonFromSentences2(self, s1: str, s2: str) -> List[str]:
        wordMap = Counter(s1.split() + s2.split())
        return [word for word in wordMap if wordMap[word] == 1]

def main():
    test_cases = [
        ("this apple is sweet", "this apple is sour"), # ["sweet","sour"]
        ("apple apple", "banana"), # ["banana"]
        ("s z z z s", "s z ejt"), # ["ejt"]
        ("ppz wl ppz", "wl e b b") # ["e"]
    ]
    solution = Solution()
    for i, (s1, s2) in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input s1:", s1)
        print("Input s2:", s2)
        print("Output:", solution.uncommonFromSentences2(s1, s2))
        print()

if __name__ == "__main__":
    main()