# First Unique Character in a String - Easy
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        numMap = Counter(s)
        for i, char in enumerate(s):
            if numMap[char] == 1:
                return i
        return -1

def main():
    test_cases = [
        "leetcode", # 0
        "loveleetcode", # 2
        "aabb" # -1
    ]
    solution = Solution()
    for i, s in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input s:", s)
        print("Output:", solution.firstUniqChar(s))
        print()

if __name__ == "__main__":
    main()