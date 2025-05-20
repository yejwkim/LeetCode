# Isomorphic Strings
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        numMapS: dict[str, str] = {}
        for i, char in enumerate(s):
            if (char in numMapS and numMapS[char] != t[i]):
                return False
            numMapS[char] = t[i]
        numMapT: dict[str, str] = {}
        for i, char in enumerate(t):
            if (char in numMapT and numMapT[char] != s[i]):
                return False
            numMapT[char] = s[i]
        return True
    
    def isIsomorphic2(self, s: str, t: str) -> bool: 
        d = {}
        visted = set()
        for i, char in enumerate(s):
            if char not in d:
                if t[i] in visted:
                    return False
                d[char] = t[i]
                visted.add(t[i])
            else:
                if d[char] != t[i]:
                    return False
        return True

def main():
    test_cases = [
        ("egg", "add"), # true
        ("foo", "bar"), # false
        ("paper", "title"), # true
        ("badc", "baba") # false
    ]
    solution = Solution()
    for i, (s, t) in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input arr1:", s)
        print("Input arr2:", t)
        print("Output:", solution.isIsomorphic3(s, t))
        print()

if __name__ == "__main__":
    main()