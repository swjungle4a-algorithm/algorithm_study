from collections import deque

def bfs(x, n, arr):
    visited = [0] * n
    visited[x] = 1
    q = deque([x])
    
    while q:
        x = q.popleft()
        for i in arr[x]:
            if not visited[i]:
                visited[i] = visited[x] + 1
                q.append(i)
                
    return visited.count(max(visited))

def solution(n, edge):
    arr = [[] * n for _ in range(n)]
    
    for x, y in edge:
        x, y = x-1, y-1
        arr[x].append(y)
        arr[y].append(x)
    
    return bfs(0, n, arr)
