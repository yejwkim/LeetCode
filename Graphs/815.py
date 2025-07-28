# Bus Routes - Hard
from typing import List
from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        graph = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                graph[stop].append(i)
        if source not in graph or target not in graph:
            return -1
        visited_routes = set()
        visited_stops = {source}
        queue = deque([source])
        bus = 0
        while queue:
            bus += 1
            for _ in range(len(queue)):
                stop = queue.popleft()
                for route_idx in graph[stop]:
                    if route_idx in visited_routes:
                        continue
                    visited_routes.add(route_idx)
                    for nxt_stop in routes[route_idx]:
                        if nxt_stop == target:
                            return bus
                        if nxt_stop not in visited_stops:
                            visited_stops.add(nxt_stop)
                            queue.append(nxt_stop)
        return -1