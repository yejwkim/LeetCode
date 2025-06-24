# Median of Two Sorted Arrays - Hard
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float: # O(m + n)
        arr: List[int] = []
        m, n = len(nums1), len(nums2)
        i = j = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1
        if i < m:
            arr.extend(nums1[i:])
        if j < n:
            arr.extend(nums2[j:])
        if len(arr) % 2 == 1:
            return arr[len(arr) // 2]
        else:
            return (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) / 2

    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float: # O((m + n)^2)
        k = (len(nums1) + len(nums2)) // 2 + 1
        median = float('inf')
        odd = (len(nums1) + len(nums2)) % 2 == 1
        def min_array(nums1: List[int], nums2: List[int], i: int, odd: bool) -> float:
            arr: List[int] = []
            m, n = len(nums1), len(nums2)
            i = j = 0
            while i < m and j < n:
                if nums1[i] <= nums2[j]:
                    arr.append(nums1[i])
                    i += 1
                else:
                    arr.append(nums2[j])
                    j += 1
            if i < m:
                arr.extend(nums1[i:])
            if j < n:
                arr.extend(nums2[j:])
            if odd:
                return arr[-1]
            else:
                return (arr[-1] + arr[-2]) / 2
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            median = min(median, min_array(nums1[:i], nums2[:(k - i)], i, odd))
        return median

    def findMedianSortedArrays3(self, nums1: List[int], nums2: List[int]) -> float: # O(log(m+n))
        def find_kth(nums1, nums2, k):
            i = j = 0
            while True:
                if i == len(nums1):
                    return nums2[j + k - 1]
                if j == len(nums2):
                    return nums1[i + k - 1]
                if k == 1:
                    return min(nums1[i], nums2[j])

                step = k // 2
                new_i = min(i + step, len(nums1)) - 1
                new_j = min(j + step, len(nums2)) - 1

                if nums1[new_i] <= nums2[new_j]:
                    k -= (new_i - i + 1)
                    i = new_i + 1
                else:
                    k -= (new_j - j + 1)
                    j = new_j + 1

        total = len(nums1) + len(nums2)
        if total % 2:
            return find_kth(nums1, nums2, total // 2 + 1)
        else:
            return (find_kth(nums1, nums2, total // 2) +
                    find_kth(nums1, nums2, total // 2 + 1)) / 2

    def findMedianSortedArrays4(self, nums1: List[int], nums2: List[int]) -> float: # O(log(m+n))
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays4(nums2, nums1)
        len1, len2 = len(nums1), len(nums2)
        left, right = 0, len(nums1)
        while left <= right:
            part1 = (left + right) // 2
            part2 = (len1 + len2 + 1) // 2 - part1
            max_left1 = float('-inf') if part1 == 0 else nums1[part1 - 1]
            min_right1 = float('inf') if part1 == len1 else nums1[part1]
            max_left2 = float('-inf') if part2 == 0 else nums2[part2 - 1]
            min_right2 = float('inf') if part2 == len2 else nums2[part2]
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if (len1 + len2) % 2 == 0:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
                else:
                    return max(max_left1, max_left2)
            elif max_left1 > min_right2:
                right = part1 - 1
            else:
                left = part1 + 1
        return -1

def main():
    test_cases = [
        ([1,3], [2]), # 2.0000
        ([1,2], [3,4]), # 2.5000
        ([1,4,7], [3,6]), # 4.0000
        ([2,3,7,9,10,12], [1,4,5,6,8,11]) # 6.5000
    ]
    solution = Solution()
    for i, (nums1, nums2) in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input nums1:", nums1)
        print("Input nums2:", nums2)
        print("Output:", solution.findMedianSortedArrays4(nums1, nums2))
        print()

if __name__ == "__main__":
    main()