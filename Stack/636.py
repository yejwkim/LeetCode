# Exclusive Time of Functions - Medium
from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res: List[int] = [0] * n
        stack: List[int] = []
        prev_time = 0
        for log in logs:
            func, action, time = log.split(":")
            if action == "start":
                if stack:
                    res[stack[-1]] += int(time) - prev_time
                stack.append(int(func))
                prev_time = int(time)
            else:
                res[stack.pop()] += int(time) - prev_time + 1
                prev_time = int(time) + 1
        return res

def main():
    test_cases = [
        (2, ["0:start:0","1:start:2","1:end:5","0:end:6"]), # [3,4]
        (1, ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]), # [8]
        (2, ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]) # [7,1]
    ]
    solution = Solution()
    for i, (n, logs) in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input n:", n)
        print("Input logs:", logs)
        print("Output:", solution.exclusiveTime(n, logs))
        print()

if __name__ == "__main__":
    main()