# Sqrt(x) - Easy

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square > x:
                right = mid - 1
            elif square < x:
                left = mid + 1
            else:
                return mid
        return right
        
def main():
    test_cases = [
        4, # 2
        8, # 2
        27 # 5
    ]
    solution = Solution()
    for i, x in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input x:", x)
        print("Output:", solution.mySqrt(x))
        print()

if __name__ == "__main__":
    main()