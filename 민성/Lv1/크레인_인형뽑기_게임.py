def solution(board, moves):
    answer = 0

    stk = []
    len_board = len(board)
    
    for num in moves:   
        col = num-1

        for row in range(0,len_board):
            if board[row][col]:
                if stk and board[row][col] == stk[-1]:
                    stk.pop()
                    board[row][col] = 0
                    answer+=2
                    break
                    
                stk.append(board[row][col])
                board[row][col] = 0
                break  
    return answer
