# Daily Temperatures - Medium
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res: List[int] = [0] * len(temperatures)
        stack: List[int] = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = i - prev
            stack.append(i)
        return res
    
def main():
    test_cases = [
        [73,74,75,71,69,72,76,73], # [1,1,4,2,1,1,0,0]
        [30,40,50,60], # [1,1,1,0]
        [30,60,90], # [1,1,0]
    ]
    solution = Solution()
    for i, temperatures in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input temperatures:", temperatures)
        print("Output:", solution.dailyTemperatures(temperatures))
        print()

if __name__ == "__main__":
    main()