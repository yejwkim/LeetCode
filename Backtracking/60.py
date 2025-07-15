# Permutation Sequence - Hard
class Solution:
    def getPermutation(self, n: int, k: int) -> str: # Initial Approach; Terrible efficiency
        nums = [str(i) for i in range(1, n + 1)]
        res = []
        def backtrack(start):
            if start == n:
                res.append("".join(nums))
                return
            for i in range(start, n):
                nums[i], nums[start] = nums[start], nums[i]
                backtrack(start + 1)
                nums[i], nums[start] = nums[start], nums[i]
        backtrack(0)
        res.sort()
        return res[k - 1]