from sys import maxsize
from heapq import heappop, heappush
INF = maxsize

def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N+1)]
    distance = [maxsize for _ in range(N+1)]
    que = []
    
    for s, e, d in road :
        graph[s].append((d, e))
        graph[e].append((d, s))
    
    heappush(que, (0, 1))
    distance[1] = 0
    while que :
        od, s = heappop(que)
        if distance[s] < od :
            continue
        for d, e in graph[s] :
            nd = od + d
            if distance[e] > nd :
                distance[e] = nd
                heappush(que, (nd, e))
    answer = sum(map(lambda x: 1 if x <= K else 0, distance[1:]))
    return answer 
