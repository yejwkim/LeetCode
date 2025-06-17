# Peak Index in a Mountain Array - Medium
from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left

def main():
    test_cases = [
        [0,1,0], # 1
        [0,2,1,0], # 1
        [0,5,10,2], # 2
        [3,9,8,6,4] # 1
    ]
    solution = Solution()
    for i, arr in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input arr:", arr)
        print("Output:", solution.peakIndexInMountainArray(arr))
        print()

if __name__ == "__main__":
    main()