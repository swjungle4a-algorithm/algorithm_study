def solution(board, moves):
    answer = 0
    len_board = len(board) # 배열 크기
    
    stack = [] # 뽑을 인형 담을 스택
    
    crane_list = [[] for i in range(len_board)]
    
    for i in range(len_board-1, -1, -1):
        for j in range(len_board):
            tmp = board[i][j]
            if tmp != 0:
                crane_list[j].append(tmp)
            
    # 뽑을 위치에서 0일 경우 인형이 있는 위치까지 찾아야 함
    
    for num in moves:
        
        i = num-1
        
        if not crane_list[i]:
            continue
            
        now = crane_list[i].pop()
        
        stack.append(now)
        
        while True:
            
            if len(stack) < 2:
                break
                
            if stack[-1] != stack[-2]:
                break
            else:
                stack.pop()
                stack.pop()
                answer += 2
                   
    return answer
