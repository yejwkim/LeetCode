# Create Maximum Number - Hard
from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def pick_max(nums: List[int], t: int) -> List[int]:
            drop = len(nums) - t
            stack: List[int] = []
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:t]
        
        def merge(a: List[int], b: List[int]) -> List[int]:
            res: List[int] = []
            while a or b:
                if a > b:
                    res.append(a.pop(0))
                else:
                    res.append(b.pop(0))
            return res
        
        best = [0] * k
        for t in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            subseq1 = pick_max(nums1, t)
            subseq2 = pick_max(nums2, k - t)
            candidate = merge(subseq1[:], subseq2[:])
            if candidate > best:
                best = candidate
        return best

def main():
    test_cases = [
        ([3,4,6,5], [9,1,2,5,8,3], 5), # [9,8,6,5,3]
        ([6,7], [6,0,4], 5), # [6,7,6,0,4]
        ([3,9], [8,9], 3), # [9,8,9]
        ([1,2,3,9], [4,9,1,2], 5), # [9,4,9,1,2]
        ([1,2,8,9], [4,9,1,2], 5) # [9,8,9,1,2]
    ]
    solution = Solution()
    for i, (nums1, nums2, k) in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input nums1:", nums1)
        print("Input nums2:", nums2)
        print("Input k:", k)
        print("Output:", solution.maxNumber(nums1, nums2, k))
        print()

if __name__ == "__main__":
    main()