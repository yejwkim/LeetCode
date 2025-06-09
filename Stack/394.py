# Decode String - Medium
from typing import List

class Solution:
    def decodeString(self, s: str) -> str:
        stack: List[str] = []
        for char in s:
            if char.isalpha():
                if stack and stack[-1].isalpha():
                    stack.append(stack.pop() + char)
                else:
                    stack.append(char)
            elif char == "]":
                temp = stack.pop()
                stack.pop()
                num = stack.pop()
                if stack and stack[-1].isalpha():
                    stack.append(stack.pop() + temp * int(num))
                else:
                    stack.append(temp * int(num))
            else:
                if char.isnumeric() and stack and stack[-1].isnumeric():
                    stack.append(stack.pop() + char)
                else:
                    stack.append(char)
        return stack[0]

    def decodeString2(self, s: str) -> str: # More clear solution
        stack: List[str] = []
        curNum = 0
        curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(str(curNum))
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + int(num)*curString
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString

def main():
    test_cases = [
        "3[a]2[bc]", # "aaabcbc"
        "3[a2[c]]", # "accaccacc"
        "2[abc]3[cd]ef", # "abcabccdcdcdef"
        "10[a]", # "aaaaaaaaaa"
        "3[a2[b4[F]c]]"
    ]
    solution = Solution()
    for i, s in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input s:", s)
        print("Output:", solution.decodeString2(s))
        print()

if __name__ == "__main__":
    main()