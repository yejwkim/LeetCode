# Minimum Cost For Tickets - Medium
from typing import List
from collections import deque

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cost = 0
        weekPass: deque[tuple[int, int]] = deque()
        monthPass: deque[tuple[int, int]] = deque()
        for day in days:
            while weekPass and weekPass[0][0] + 7 <= day:
                weekPass.popleft()
            while monthPass and monthPass[0][0] + 30 <= day:
                monthPass.popleft()
            weekPass.append((day, cost + costs[1]))
            monthPass.append((day, cost + costs[2]))
            cost = min(cost + costs[0], weekPass[0][1], monthPass[0][1])
        return cost