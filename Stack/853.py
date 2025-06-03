# Car Fleet - Medium
from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack: List[float] = []
        for pos, spd in cars:
            time = (target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)

def main():
    test_cases = [
        (12, [10,8,0,5,3], [2,4,1,1,3]), # 3
        (10, [3], [3]), # 1
        (100, [0,2,4], [4,2,1]) # 1
    ]
    solution = Solution()
    for i, (target, position, speed) in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input target:", target)
        print("Input position:", position)
        print("Input speed:", speed)
        print("Output:", solution.carFleet(target, position, speed))
        print()

if __name__ == "__main__":
    main()