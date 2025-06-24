# Search a 2D Matrix - Medium
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: # O(log n)
        m, n = len(matrix), len(matrix[0])
        row_left, row_right = 0, m - 1
        while row_left < row_right:
            row_mid = (row_left + row_right) // 2
            if matrix[row_mid][0] > target:
                row_right = row_mid - 1
            elif matrix[row_mid][-1] < target:
                row_left = row_mid + 1
            else:
                row_left = row_right = row_mid
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row_left][mid] == target:
                return True
            elif matrix[row_left][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

def main():
    test_cases = [
        ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3), # true
        ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13), # false
        ([[1]], 1) # true
    ]
    solution = Solution()
    for i, (matrix, target) in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input matrix:", matrix)
        print("Input target:", target)
        print("Output:", solution.searchMatrix(matrix, target))
        print()

if __name__ == "__main__":
    main()