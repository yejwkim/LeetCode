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
    
    def getPermutation2(self, n: int, k: int) -> str:
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i
        k -= 1
        nums = [str(i) for i in range(1, n + 1)]
        result = []
        for pos in range(n, 0, -1):
            idx, k = divmod(k, fact[pos - 1])
            print(pos, idx, k, nums[idx])
            result.append(nums.pop(idx))
        return "".join(result)

def main():
    solution = Solution()
    print(solution.getPermutation2(3, 3))
    print(solution.getPermutation2(4, 9))
    print(solution.getPermutation2(3, 1))

if __name__ == "__main__":
    main()