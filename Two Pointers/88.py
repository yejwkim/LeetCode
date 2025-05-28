# Merge Sorted Array - Easy
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, p = m - 1, n - 1, m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -=1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p -= 1
            p2 -= 1

def main():
    test_cases = [
        ([1,2,3,0,0,0],3,[2,5,6],3), # [1,2,2,3,5,6]
        ([1],1,[],0), # [1]
        ([0],0,[1],1) # [1]
    ]
    solution = Solution()
    for i, (nums1, m, nums2, n) in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input nums1:", nums1)
        print("Input m:", m)
        print("Input nums2:", nums2)
        print("Input n:", n)
        solution.merge(nums1, m, nums2, n)
        print("Output:", nums1)
        print()

if __name__ == "__main__":
    main()