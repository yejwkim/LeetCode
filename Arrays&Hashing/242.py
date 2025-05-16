# Valid Anagram - Easy
class Solution:
    def isAnagram(self, s: str, t: str) -> bool: # Hashmap
        if (len(s) != len(t)):
            return False
        numMap: dict[str, int] = {}
        for char in s:
            if char in numMap:
                numMap[char] += 1
            else:
                numMap[char] = 1
        for char in t:
            if char not in numMap:
                return False
            if numMap[char] == 0:
                return False
            numMap[char] -= 1
        return True

    def isAnagram2(self, s: str, t: str) -> bool: # Hashtable
        count = [0] * 26
        for x in s:
            count[ord(x) - ord('a')] += 1
        for x in t:
            count[ord(x) - ord('a')] -= 1
        for val in count:
            if val != 0:
                return False
        return True
    
def main():
    test_cases = [
        ("anagram", "nagaram"), # True
        ("rat", "car") # False
    ]
    solution = Solution()
    for i, (s, t) in enumerate(test_cases):
        print(f"Test Case {i+1}:")
        print("Input s:", s)
        print("Input t:", t)
        print("Output:", solution.isAnagram(s, t))
        print()
        
if __name__ == "__main__":
    main()