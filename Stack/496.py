# Next Greater Element I - Easy
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res: List[int] = []
        stack: List[int] = []
        numMap: dict[int, int] = {}
        for elem in nums2:
            while stack and elem > stack[-1]:
                numMap[stack.pop()] = elem
            stack.append(elem)
        while stack:
            numMap[stack.pop()] = -1
        for elem in nums1:
            res.append(numMap[elem])
        return res
    
def main():
    test_cases = [
        ([4,1,2], [1,3,4,2]), # [-1,3,-1]
        ([2,4], [1,2,3,4]) # [3,-1]
    ]
    solution = Solution()
    for i, (nums1, nums2) in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input nums1:", nums1)
        print("Input nums2:", nums2)
        print("Output:", solution.nextGreaterElement(nums1, nums2))
        print()

if __name__ == "__main__":
    main()