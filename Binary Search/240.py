# Search a 2D Matrix II - Medium
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: # Staircase O(m + n)
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False

    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool: # Binary Search O(m log n)
        for row in matrix:
            if row[0] > target:
                break
            if row[0] <= target and row[-1] >= target:
                left, right = 0, len(row) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if row[mid] == target:
                        return True
                    if row[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
        return False

def main():
    test_cases = [
        ([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5), # true
        ([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20), # false
        ([[1,3,5]], -1) # false
    ]
    solution = Solution()
    for i, (matrix, target) in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input matrix:", matrix)
        print("Input target:", target)
        print("Output:", solution.searchMatrix2(matrix, target))
        print()

if __name__ == "__main__":
    main()