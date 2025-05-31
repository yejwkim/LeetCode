# Longest Repeating Character Replacement - Medium
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        strMap: dict[str, int] = defaultdict(int)
        left = 0
        maxLength = 0
        for right in range(len(s)):
            strMap[s[right]] += 1
            if (right - left + 1) - max(strMap.values()) > k:
                strMap[s[left]] -= 1
                left += 1
            else:
                maxLength = max(maxLength, (right - left + 1))
        return maxLength
    
def main():
    test_cases = [
        ("ABAB",2), # 4
        ("AABABBA",1), # 4
        ("ABCDE",1), # 2
        ("AABABBA",2), # 5
    ]
    solution = Solution()
    for i, (s, k) in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input s:", s)
        print("Input k:", k)
        print("Output:", solution.characterReplacement(s, k))
        print()
        
if __name__ == "__main__":
    main()