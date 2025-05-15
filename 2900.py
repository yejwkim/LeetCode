# Longest Unequal Adjacent Groups Subsequence I - Easy
from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = [words[0]]
        prev = groups[0]
        for i in range(1, len(words)):
            if (groups[i] != prev):
                res.append(words[i])
                prev = groups[i]
        return res

    def getLongestSubsequenceBest(self, words: List[str], groups: List[int]) -> List[str]:
        result = []
        last = -1
        for i in range(len(words)):
            if groups[i] != last:
                result.append(words[i])
                last = groups[i]
        return result

def main():
    test_cases = [
        (["e", "a", "b"], [0, 0, 1]), # ["e", "b"]
        (["a", "b", "c", "d"], [1, 0, 1, 1]), # ["a", "b", "c"]
        (["a", "b", "c", "d"], [0, 0, 1, 1]) # ["a", "c"]
    ]
    solution = Solution()
    for i, (words, groups) in enumerate(test_cases):
        result = solution.getLongestSubsequence(words, groups)
        print(f"Test Case {i+1}:")
        print("Input words:", words)
        print("Input groups:", groups)
        print("Output:", result)
        print()
        
if __name__ == "__main__":
    main()