# Trapping Rain Water - Hard
from typing import List

class Solution:
    # def trap(self, height: List[int]) -> int: # Doesn't Work
    #     if len(height) == 1:
    #         return 0
    #     left, right = 0, 1
    #     total = 0
    #     while height[left] == 0:
    #         left += 1
    #         right += 1
    #     while left < len(height):
    #         while right < len(height) and height[left] > height[right]:
    #             right += 1
    #         if right == len(height):
    #             left += 1
    #             right = left + 1
    #         elif left + 1 == right:
    #             left += 1
    #             right += 1
    #         else:
    #             temp_total = height[left] * (right - left - 1)
    #             print(left, right, temp_total)
    #             for i in range(left + 1, right):
    #                 temp_total -= height[i]
    #             total += temp_total
    #             left = right
    #             right += 1
    #     return total

    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        total = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    total += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    total += right_max - height[right]
                right -= 1
        return total

def main():
    test_cases = [
        [0,1,0,2,1,0,1,3,2,1,2,1], # 6
        [4,2,0,3,2,5], # 9
        [0,3,2,0,1,2,1], # 3
        [0,1,0,1,2,3,0,1], # 2
        [3,1,2], # 1
        [0,2,2,1,3], # 1
        [2,1,1,3] # 2
    ]
    solution = Solution()
    for i, height in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input height:", height)
        print("Output:", solution.trap(height))
        print()

if __name__ == "__main__":
    main()