# Split Array Largest Sum - Hard
from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            cur_sum = 0
            cur_k = 1
            for num in nums:
                if cur_sum + num > mid:
                    cur_k += 1
                    cur_sum = 0
                cur_sum += num
                if cur_k > k:
                    break
            if cur_k <= k:
                right = mid
            else:
                left = mid + 1
        return left

def main():
    test_cases = [
        ([7,2,5,10,8], 2), # 18
        ([1,2,3,4,5], 2), # 9
        ([1,4,4], 3) # 4
    ]
    solution = Solution()
    for i, (nums, k) in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input nums:", nums)
        print("Input k:", k)
        print("Output:", solution.splitArray(nums, k))
        print()

if __name__ == "__main__":
    main()