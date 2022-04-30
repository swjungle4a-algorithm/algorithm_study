def solution(board, moves):
    answer = 0
    stack = []
    
    for i in moves:
        idx = i - 1
        for j in range(len(board)):
            if board[j][idx] != 0: 
                stack.append(board[j][idx])
                board[j][idx] = 0
                break
                
        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer += 2
    
    return answer