from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    
    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)
    
    dist = [0] * (n+1)
    que = deque([1])
    
    while que:
        start = que.popleft()
        for i in graph[start]:
            if dist[i] == 0:
                dist[i] = dist[start] + 1
                que.append(i)
    max_val = max(dist)
    for i in range(2, len(dist)):
        if max_val == dist[i]:
            answer += 1
    return answer
