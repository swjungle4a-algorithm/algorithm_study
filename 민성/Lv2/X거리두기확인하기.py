from collections import deque
def solution(places):
    answer = [1] * 5

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    def bfs(a,b):
        q = deque()
        q.append((a,b,0))
        
        while q:
            x,y, cost = q.popleft()
            
            if place[x][y] == 'P' and 0<cost<=2: 
                return True
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny]:
                    visited[nx][ny] = 1              
                    # 
                    q.append((nx,ny,cost))      
        return False  
    
    for idx, place in enumerate(places):
        visited = [[0]*5 for _ in range(5)]
        
        res = False
        for i in range(5):
            for j in range(5):
                if not visited[i][j] and place[i][j] == 'P':
                    visited[i][j] = 1
                    res = bfs(i,j)
                    if res:
                        break
            if res:
                break             
        if res:
            answer[idx] = 0
        
    return answer
