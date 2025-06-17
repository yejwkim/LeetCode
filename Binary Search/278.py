# First Bad Version - Easy
bad = 4
def isBadVersion(version: int) -> bool:
    return version >= bad

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

def main():
    global bad
    s = Solution()
    bad = 4
    print("Test 1:", s.firstBadVersion(5))

if __name__ == "__main__":
    main()