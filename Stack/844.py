# Backspace String Compare - Easy
from functools import reduce

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool: # Using SC O(n)
        stackS: list[str] = []
        stackT: list[str] = []
        for char in s:
            if char != "#":
                stackS.append(char)
            elif stackS:
                stackS.pop()
        for char in t:
            if char != "#":
                stackT.append(char)
            elif stackT:
                stackT.pop()
        return "".join(stackS) == "".join(stackT)

    def backspaceCompare2(self, s: str, t: str) -> bool: # Using SC O(n)
        def back(res, c):
            if c != '#': res.append(c)
            elif res: res.pop()
            return res
        return reduce(back, s, []) == reduce(back, t, [])

    def backspaceCompare3(self, s: str, t: str) -> bool: # Using SC O(1); Two-Pointers
        def next_valid_char(s: str, index: int):
            skip = 0
            while index >= 0:
                if s[index] == '#':
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    break
                index -= 1
            return index
        
        i, j = len(s) - 1, len(t) - 1
        
        while i >= 0 or j >= 0:
            i = next_valid_char(s, i)
            j = next_valid_char(t, j)
            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            if (i >= 0) != (j >= 0):
                return False
            i -= 1
            j -= 1
        return True

def main():
    test_cases = [
        ("ab#c", "ad#c"), # true
        ("ab##", "c#d#"), # true
        ("a#c", "b"), # false
        ("y#fo##f", "y#f#o##f") # true
    ]
    solution = Solution()
    for i, (s, t) in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input s:", s)
        print("Input t:", t)
        print("Output:", solution.backspaceCompare3(s, t))
        print()

if __name__ == "__main__":
    main()