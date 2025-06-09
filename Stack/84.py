# Largest Rectangle in Histogram - Hard
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        next_smaller: List[int] = [len(heights)] * len(heights)
        prev_smaller: List[int] = [-1] * len(heights)
        stack: List[int] = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                next_smaller[stack.pop()] = i
            if stack:
                prev_smaller[i] = stack[-1]
            stack.append(i)
        max_area = 0
        for i, height in enumerate(heights):
            max_area = max(max_area, (next_smaller[i] - prev_smaller[i] - 1) * height)
        return max_area

    def largestRectangleArea2(self, heights: List[int]) -> int: # One-pass solution
        heights.append(0)
        stack: List[int] = []
        max_area = 0
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area

def main():
    test_cases = [
        [2,1,5,6,2,3], # 10
        [2,4], # 4
        [2,1,5,6,4,2,3] # 12
    ]
    solution = Solution()
    for i, heights in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input heights:", heights)
        print("Output:", solution.largestRectangleArea2(heights))
        print()

if __name__ == "__main__":
    main()