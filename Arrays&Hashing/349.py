# Intersection of Two Arrays - Easy
from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

def main():
    test_cases = [
        ([1,2,2,1], [2,2]), # [2]
        ([4,9,5], [9,4,9,8,4]) # [9,4]
    ]
    solution = Solution()
    for i, (nums1, nums2) in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input nums1:", nums1)
        print("Input nums2:", nums2)
        print("Output:", solution.intersection(nums1, nums2))
        print()

if __name__ == "__main__":
    main()