import heapq
from collections import defaultdict

def solution(N, road, K):
    
    road_info = defaultdict(list)
    
    for roads in road:
        
        start, end, cost = roads
        
        road_info[start].append((cost, start, end))
        road_info[end].append((cost, end, start))
    
    INF = 1e9
    
    min_cost = [INF for _ in range(N+1)]
    
    q = []
    
    for tmp in road_info[1]:
        heapq.heappush(q, tmp)
        
    min_cost[1] = 0
    
    while q:
        now_cost, s, d = heapq.heappop(q)
        if min_cost[s] + now_cost < min_cost[d]:
            min_cost[d] = min_cost[s] + now_cost
            for tmp in road_info[d]:
                heapq.heappush(q, tmp)
                
    answer = 0
    for num in min_cost:
        if num <= K:
            answer += 1
    return answer
