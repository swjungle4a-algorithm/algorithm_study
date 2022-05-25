from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0 for _ in range(m)] for __ in range(n)]
    answer = 0
    
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    
    que = deque()
    que.append((0,0))
    visited[0][0] = 1
    while que :
        r, c = que.popleft()
        
        for i in range(4) :
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0 <= nr < n and 0 <= nc < m:
                if maps[nr][nc] and not visited[nr][nc]:
                    visited[nr][nc] = visited[r][c] + 1
                    que.append((nr,nc))
    answer = visited[n-1][m-1] if visited[n-1][m-1] else -1
    return answer
