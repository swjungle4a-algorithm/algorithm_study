import heapq
from collections import defaultdict

def solution(n, costs):

    max_cost = 1e9
    costlist = [max_cost] * n
    visited = set()
    graph = defaultdict(list)
    q = []
    for start, end, cost in costs:
        graph[start].append((cost, end))
        graph[end].append((cost, start))
    
    heapq.heappush(q, (0, 0))
    costlist[0] = 0
    
    while q:
        c, now = heapq.heappop(q)
        visited.add(now)
        for next_cost, new in graph[now]:
            if new not in visited and next_cost < costlist[new]:
                costlist[new] = next_cost
                heapq.heappush(q, (next_cost, new))
            
    return sum(costlist)
