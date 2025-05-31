# Minimum Window Substring - Hard
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        numMap: dict[str, int] = {}
        for char in t:
            if char not in numMap:
                numMap[char] = 1
            else:
                numMap[char] += 1
        minLength = len(s) + 1
        minStr = ""
        diff = len(t)
        left = 0
        while left < len(s) and s[left] not in numMap:
            left += 1
        for right in range(left, len(s)):
            if s[right] not in numMap:
                continue
            if numMap[s[right]] > 0:
                diff -= 1
            numMap[s[right]] -= 1
            while diff == 0:
                if (right - left + 1) < minLength:
                    minStr = s[left:right + 1]
                    minLength = right - left + 1
                if numMap[s[left]] == 0:
                    diff += 1
                numMap[s[left]] += 1
                left += 1
                while left < right and s[left] not in numMap:
                    left += 1
        return minStr

def main():
    test_cases = [
        ("ADOBECODEBANC", "ABC"), # "BANC"
        ("a", "a"), # "a"
        ("a", "aa"), # ""
        ("LEETCODE", "TCE") # "ETC"
    ]
    solution = Solution()
    for i, (s, t) in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input s:", s)
        print("Input t:", t)
        print("Output:", solution.minWindow(s, t))
        print()

if __name__ == "__main__":
    main()