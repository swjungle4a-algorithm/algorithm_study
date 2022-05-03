''' python
from collections import deque

def bfs(place, visited, x, y):
    q = deque([[x, y]])
    visited[x][y] = True
    
    while q:
        x, y = q.popleft()
        
        for i in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nx = x + i[0]
            ny = y + i[1]
            
            if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == -1 and place[nx][ny] != "X":
                if place[nx][ny] == "O":
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])

                if place[nx][ny] == "P" and visited[x][y] <= 2:
                    return False
                    
    return True
                
def solution(places):
    answer = []
    
    for place in places:
        flag = True
        visited = [[-1] * 5 for _ in range(5)]
        
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P" and visited[i][j] == -1:
                    flag = bfs(place, visited, i, j)
                    if not flag:
                        break
            if not flag:
                break

        answer.append(1) if flag else answer.append(0)
            
    return answer
'''
