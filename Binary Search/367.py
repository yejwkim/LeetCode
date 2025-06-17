# Valid Perfect Square - Easy
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        while left <= right:
            mid = (left + right) // 2
            if mid * mid > num:
                right = mid - 1
            elif mid * mid < num:
                left = mid + 1
            else:
                return True
        return False
    
def main():
    test_cases = [
        16, # true
        14 # false
    ]
    solution = Solution()
    for i, num in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input num:", num)
        print("Output:", solution.isPerfectSquare(num))
        print()

if __name__ == "__main__":
    main()