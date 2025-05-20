# Relative Sort Array
from typing import List
import collections

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]: # O(n^2)
        res = []
        numMap = collections.Counter(arr1)
        for elem in arr2:
            while numMap[elem] > 0:
                res.append(elem)
                arr1.remove(elem) # This forces the algorithm to be O(n^2)
                numMap[elem] -= 1
        res += sorted(arr1)
        return res
    
    def relativeSortArray2(self, arr1: List[int], arr2: List[int]) -> List[int]: # O(n log n)
        count = collections.Counter(arr1)
        res = []
        for num in arr2:
            res.extend([num] * count[num])
            del count[num]
        remaining = []
        for num, freq in count.items():
            remaining.extend([num] * freq)
        res.extend(sorted(remaining))
        return res
    
def main():
    test_cases = [
        ([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]), # [2,2,2,1,4,3,3,9,6,7,19]
        ([28,6,22,8,44,17], [22,28,8,6]) # [22,28,8,6,17,44]
    ]
    solution = Solution()
    for i, (arr1, arr2) in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input arr1:", arr1)
        print("Input arr2:", arr2)
        print("Output:", solution.relativeSortArray2(arr1, arr2))
        print()

if __name__ == "__main__":
    main()