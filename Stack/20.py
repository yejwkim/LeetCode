# Valid Parentheses - Easy

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketDict = {"]":"[", ")":"(", "}":"{"}
        for char in s:
            if char in bracketDict.values():
                stack.append(char)
            elif char in bracketDict:
                if not stack or bracketDict[char] != stack.pop():
                    return False
            else:
                return False
        return not stack

def main():
    test_cases = [
        "()", # true
        "()[]{}", # true
        "(]", # false
        "([])" # true
    ]
    solution = Solution()
    for i, s in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input s:", s)
        print("Output:", solution.isValid(s))
        print()

if __name__ == "__main__":
    main()