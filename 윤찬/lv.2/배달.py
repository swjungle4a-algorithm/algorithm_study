import heapq
def solution(N, road, K):
    answer = 1
    graph = [[]*(N+1) for _ in range(N+1)]
    for start, end, cost in road:
        if cost > K: continue
        graph[start].append((cost, end))
        graph[end].append((cost, start))
        
    arr = []
    tmp = [1e9] * (N+1)
    for i in graph[1]:
        heapq.heappush(arr, i)

    while arr:
        dist, node = heapq.heappop(arr)
        if dist > K: continue
        if tmp[node] <= K: continue
        tmp[node] = dist
        
        for cost, start in graph[node]:
            cost += dist
            heapq.heappush(arr, (cost, start))

    for i in tmp[2:]:
        if i > K: continue
        answer += 1
        
    return answer
