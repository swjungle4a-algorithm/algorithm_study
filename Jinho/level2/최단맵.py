from collections import deque

def solution(maps):
    answer = 0
    
    q = deque([(0,0)])

    n = len(maps) # 행
    m = len(maps[0]) # 열
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q:
        
        x, y = q.popleft()

        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0<= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                
                q.append((nx, ny))
                
                maps[nx][ny] = maps[x][y] + 1

    answer = maps[n-1][m-1]
    return answer if answer != 1 else -1
