from collections import deque
import heapq
dx = [-1,1,0,0]
dy = [0,0,-1,1]

answer = 0

def bfs(maps):
    row = len(maps)
    col = len(maps[0])

    hq = []
    heapq.heappush(hq,(1,0,0)) 
    
    visited = [[False]*col for _ in range(row)]
    visited[0][0] = True
    while hq:
        
        cost,r,c = heapq.heappop(hq)
        
        if r==row-1 and c == col-1:
            return cost
        
        for i in range(4):
            rx = dx[i] + r
            ry = dy[i] + c
            
            if 0<=rx<row and 0<=ry<col and not visited[rx][ry] and maps[rx][ry]:
                visited[rx][ry] = True
                heapq.heappush(hq,(cost+1,rx,ry))
    return -1
    
def solution(maps):
    answer = bfs(maps)
    return answer
