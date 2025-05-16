# Longest Unequal Adjacent Groups Subsequence II - Medium
from typing import List

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        return []
    
def main():
    test_cases = [
        (["bab", "dab", "cab"], [1, 2, 2]), # ["bab", "dab"]
        (["a", "b", "c", "d"], [1, 2, 3, 4]), # ["a", "b", "c", "d"]
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