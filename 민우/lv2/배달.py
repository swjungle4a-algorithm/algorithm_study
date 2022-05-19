import heapq
INF = float('inf')

def dijkstra(graph, dist, start):
    heap = []
    heapq.heappush(heap, [0, start])
    dist[start] = 0
    
    while heap:
        cost, curr = heapq.heappop(heap)
        
        for next_cost, next_node in graph[curr]:    
            price = cost + next_cost
            if price < dist[next_node]:
                dist[next_node] = price
                heapq.heappush(heap, [price, next_node])
    
    return dist

def solution(N, road, K):
    dist = [INF] * (N+1)
    graph = [[] for _ in range(N+1)]
    
    for x, y, c in road:
        graph[x].append([c, y])
        graph[y].append([c, x])
        
    answer = len(list(filter(lambda x : x <= K, dijkstra(graph, dist, 1))))
    return answer
