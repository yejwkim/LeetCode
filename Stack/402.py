# Remove K Digits - Medium
from typing import List

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        stack: List[str] = []
        numPop = 0
        for char in num:
            while stack and int(stack[-1]) > int(char) and numPop < k: # integer conversion not required
                stack.pop()
                numPop += 1
            stack.append(char)
        while numPop < k:
            stack.pop()
            numPop += 1
        res = "".join(stack).lstrip("0")
        return res if res else "0"

    def removeKdigits2(self, num: str, k: int) -> str: # More efficient solution
        res: List[str] = []
        for i in num:
            while k and res and res[-1]>i:
                res.pop()
                k-=1
            res.append(i)
        res=res[:len(res)-k]
        return ''.join(res).lstrip('0') or '0'

def main():
    test_cases = [
        ("1432219", 3), # "1219"
        ("10200", 1), # "200"
        ("10", 2), # "0"
        ("7420999", 3), # "999"
        ("7420999", 2), # "20999"
        ("11234", 3), # "11"
    ]
    solution = Solution()
    for i, (num, k) in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input num:", num)
        print("Input k:", k)
        print("Output:", solution.removeKdigits(num, k))
        print()

if __name__ == "__main__":
    main()