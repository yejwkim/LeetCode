# Maximum Manhattan Distance After K Changes - Medium
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ans = north = east = south = west = 0
        for i, char in enumerate(s):
            if char == "N":
                north += 1
            elif char == "E":
                east += 1
            elif char == "S":
                south += 1
            else:
                west += 1
            x = abs(west - east)
            y = abs(north - south)
            MD = x + y
            possibleMaxMD = i + 1
            maxMD = MD + min(2 * k, possibleMaxMD - MD)
            ans = max(ans, maxMD)
        return ans