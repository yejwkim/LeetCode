# Reconstruct Itinerary - Hard
from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        tickets.sort(reverse = True)
        for s, d in tickets:
            graph[s].append(d)
        route = []
        def visit(airport):
            print(airport)
            while graph[airport]:
                visit(graph[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]