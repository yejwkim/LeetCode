# Remove All Adjacent Duplicates In String - Easy
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack: list[str] = []
        for char in s:
            if not stack:
                stack.append(char)
            elif char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)

def main():
    test_cases = [
       "abbaca", # "ca"
       "azxxzy" # "ay"
    ]
    solution = Solution()
    for i, s in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input s:", s)
        print("Output:", solution.removeDuplicates(s))
        print()

if __name__ == "__main__":
    main()