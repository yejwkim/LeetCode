# Jewels and Stones - Easy
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for stone in stones:
            if (stone in set(jewels)):
                count += 1
        return count

def main():
    test_cases = [
        ("aA", "aAAbbbb"), # 3
        ("z", "ZZ") # 0
    ]
    solution = Solution()
    for i, (jewels, stones) in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input jewels:", jewels)
        print("Input stones:", stones)
        print("Output:", solution.numJewelsInStones(jewels, stones))
        print()

if __name__ == "__main__":
    main()