# Two Sum II - Input Array Is Sorted
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]: # O(n^2)
        slow, fast = 0, 1
        while slow < len(numbers):
            while fast < len(numbers):
                if numbers[slow] + numbers[fast] == target:
                    return [slow + 1, fast + 1]
                fast += 1
            slow += 1
            fast = slow + 1
        return []

    def twoSum2(self, numbers: List[int], target: int) -> List[int]: # O(n^2)
        left, right = 0, len(numbers) - 1
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left + 1, right + 1]
            elif curr_sum > target:
                right -= 1
            else:
                left += 1
        return []

def main():
    test_cases = [
        ([2,7,11,15], 9), # [1,2]
        ([2,3,4], 6), # [1,3]
        ([-1,0], -1) # [1,2]
    ]
    solution = Solution()
    for i, (numbers, target) in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input numbers:", numbers)
        print("Input target:", target)
        print("Output:", solution.twoSum2(numbers, target))
        print()

if __name__ == "__main__":
    main()