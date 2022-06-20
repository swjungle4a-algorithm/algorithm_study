from collections import defaultdict, deque
import heapq


def routesearch(origin, n, s, a, b, graph):
    costlist = [0] + [100000000000] * n
    costlist[s] = 0
    q = []
    heapq.heappush(q, (0, s))
    while q:
        now_cost, now = heapq.heappop(q)
        for next_cost, next in graph[now]:
            if costlist[now] + next_cost < costlist[next]:
                costlist[next] = costlist[now] + next_cost
                heapq.heappush(q, [next_cost, next])
    if origin:
        return costlist
    else:
        return costlist[a] + costlist[b]
    

def solution(n, s, a, b, fares):
    
    route = [[] for _ in range(n+1)]
    graph = defaultdict(list)
    costlist = [0] + [100000000000] * n
    costlist[s] = 0
    
    for start, end, cost in fares:
        graph[start].append((cost, end))
        graph[end].append((cost, start))
                
    totallist = [0] * (n+1)
    costlist = routesearch(s, n, s, a, b, graph)
    
    for i in range(1, n+1):
        totallist[i] = costlist[i] + routesearch(0, n, i, a, b, graph)
        
    return min(totallist[1:])
