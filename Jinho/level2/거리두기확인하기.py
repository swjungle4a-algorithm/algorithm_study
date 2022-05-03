from collections import deque
def solution(places):
    # 대기실은 5개이며, 각 대기실은 5x5
    # 가로+세로 거리가 2이하로 배치되면 안됨.
    # 응시자가 앉아있는 자리 사이로 파티션 있을 경우는 허용
    # p: 응시자, 0: 빈테이블, x: 파티션
    answer = []
    # 탐색해가지고 p인 경우에만 탐색을 진행하고
    # 거리가 2인 경우까지만 확인하면됨. 
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for place in places:
        # 테스트 케이스 하나부터
        
        flag = True
        
        for i in range(5): # 행
            for j in range(5): # 열
                # 응시자일경우만 탐색 시작함
                if place[i][j] == 'P':
                    depth = 0
                    q = deque([(i, j, depth)])
                    
                    while q:
                        
                        a, b, d = q.popleft() # i, j, depth
                        if d == 3 or place[a][b] == 'X':
                            continue
                        elif d > 0:
                            if place[a][b] == 'P':
                                answer.append(0)
                                flag = False
                                break
                            
                            for k in range(4):
                                na = a + dx[k]
                                nb = b + dy[k]
                                
                                if 0<=na<5 and 0<=nb<5:
                                    q.append((na, nb, depth+1))
                                
                if flag == False:
                    break
            if flag == False:
                break
        if flag == True:
            answer.append(1)
                        
    print(answer)
    
    return answer
