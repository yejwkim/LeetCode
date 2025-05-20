# Unique Number of Occurrences - Easy
from typing import List
import collections

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numMap = collections.Counter(arr)
        return len(numMap.values()) == len(set(numMap.values()))

def main():
    test_cases = [
        [1,2,2,1,1,3], # true
        [1,2], # false
        [-3,0,1,-3,1,1,1,-3,10,0] # true
    ]
    solution = Solution()
    for i, arr in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input arr:", arr)
        print("Output:", solution.uniqueOccurrences(arr))
        print()

if __name__ == "__main__":
    main()