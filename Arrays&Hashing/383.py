# Ransom Note - Easy
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        count = [0] * 26
        for char in magazine:
            count[ord(char) - ord('a')] += 1
        for char in ransomNote:
            if count[ord(char) - ord('a')] == 0:
                return False
            count[ord(char) - ord('a')] -= 1
        return True

def main():
    test_cases = [
        ("a","b"), # false
        ("aa", "ab"), # false
        ("aa", "aab") # true
    ]
    solution = Solution()
    for i, (ransomNote, magazine) in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input ransomNote:", ransomNote)
        print("Input magazine:", magazine)
        print("Output:", solution.canConstruct(ransomNote, magazine))
        print()

if __name__ == "__main__":
    main()