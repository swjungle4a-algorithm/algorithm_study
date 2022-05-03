from collections import deque

def solution(places):
    answer = []
    
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    
    for place in places :
        que = deque()
        visit = [[-1] * 5 for _ in range(5)]
        for i in range(5) :
            for j in range(5) :
                if place[i][j] == "P" :
                    que.append((i,j))
                    visit[i][j] = 0
        brkFlag = False
        while que :
            r, c = que.popleft()
            for i in range(4) :
                nr = r + dr[i]
                nc = c + dc[i]
                if (0 <= nr < 5 and 0 <= nc < 5) :
                    if place[nr][nc] == "O" and (visit[nr][nc] == -1 or visit[nr][nc] > visit[r][c]) :
                        que.append((nr,nc))
                        visit[nr][nc] = visit[r][c] + 1
                    elif place[nr][nc] == "P" :
                        if visit[r][c] == 1 :
                            answer.append(0)
                            brkFlag = True
                            print(*visit)
                            break
                        que.append((nr,nc))
                        visit[nr][nc] = 0
            if brkFlag : break
        else :
            answer.append(1)
        
                        
                
    return answer


# BFS로 탐색
# 큐에 담을 내용
# visit에 담을 내용
# 하나라도 거리 2 안에있는거 발견하면 끝 (0푸쉬)
# 처음에 P위치 초기화 필요
