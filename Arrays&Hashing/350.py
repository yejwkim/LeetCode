# Intersection of Two Arrays II - Easy
from typing import List
from collections import defaultdict, Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numMap: dict[int, int] = defaultdict(int)
        res = []
        for elem in nums1:
            numMap[elem] += 1
        for elem in nums2:
            if elem in numMap and numMap[elem] > 0:
                res.append(elem)
                numMap[elem] -= 1
        return res

    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numMap = Counter(nums1)
        res = []
        for elem in nums2:
            if numMap[elem] > 0:
                res.append(elem)
                numMap[elem] -= 1
        return res

def main():
    test_cases = [
        ([1,2,2,1], [2,2]), # [2,2]
        ([4,9,5], [9,4,9,8,4]) # [9,4]
    ]
    solution = Solution()
    for i, (nums1, nums2) in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input nums1:", nums1)
        print("Input nums2:", nums2)
        print("Output:", solution.intersect2(nums1, nums2))
        print()

if __name__ == "__main__":
    main()