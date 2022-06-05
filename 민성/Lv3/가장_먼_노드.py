from collections import defaultdict, deque

def bfs(graph,n):
    visited = [False] * (n+1)
    visited[1] = True
    
    dq = deque()
    dq.append([1,0])
    
    c = [0,0]
    
    while dq:
        start, cost = dq.popleft()
        
        if cost == c[0]:
            c[1] += 1
        elif cost > c[0]:
            c[0] = cost
            c[1] = 1
        else:
            continue
        
        for node in graph[start]:
            if not visited[node] :
                visited[node] = True
                dq.append([node, cost+1])
    return c[1]
    
def solution(n, edge):
    answer = 0

    graph = defaultdict(list)
    
    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)
        
    answer = bfs(graph,n)
    
    return answer
