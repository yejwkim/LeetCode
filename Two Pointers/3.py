# Longest Substring Without Repeating Characters - Medium
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: # O(n^2)
        maxLength = 0
        window = ""
        for i in range(len(s)):
            while s[i] in window:
                window = window[1:] # This code is O(n), so change is needed
            window += s[i]
            maxLength = max(maxLength, len(window))
        return maxLength

    def lengthOfLongestSubstring2(self, s: str) -> int: # O(n)
        char_set: set[str] = set()
        left = 0
        maxLength = 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            maxLength = max(maxLength, right - left + 1)
        return maxLength

def main():
    test_cases = [
        "abcabcbb", # 3
        "bbbbb", # 1
        "pwwkew", # 3
        "" # 0
    ]
    solution = Solution()
    for i, s in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input s:", s)
        print("Output:", solution.lengthOfLongestSubstring(s))
        print()

if __name__ == "__main__":
    main()