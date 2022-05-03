from collections import deque

def solution(places):
    answer = []
    
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    
    for place in places :
        que1 = deque()
        for i in range(5) :
            for j in range(5) :
                if place[i][j] == "P" :
                    que1.append((i,j))
        brkFlag = False
        while que1 :
            visit = [[-1] * 5 for _ in range(5)]
            que2 = deque()
            que2.append(que1.popleft())
            visit[que2[0][0]][que2[0][1]] = 0
            while que2 :
                r, c = que2.popleft()
                for i in range(4) :
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if (0 <= nr < 5 and 0 <= nc < 5) :
                        if place[nr][nc] != "X" and visit[nr][nc] == -1 :
                            que2.append((nr,nc))
                            visit[nr][nc] = visit[r][c] + 1
                            if place[nr][nc] == "P" and visit[nr][nc] <= 2 :
                                answer.append(0)
                                brkFlag = True
                                break
                if brkFlag : break
            if brkFlag : break
        else :
            answer.append(1)
        
                        
                
    return answer

