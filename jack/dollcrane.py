def solution(board, moves):
    answer = 0
    bucket = []
    size = len(board)
    doll = 0
    
    for move in moves :
        for i in range(size) :
            doll = board[i][move-1]
            if doll :
                board[i][move-1] = 0
                bucket.append(doll)
                if len(bucket) >= 2 and bucket[-1] == bucket[-2] :
                    bucket.pop()
                    bucket.pop()
                    answer += 2
                break
    
    return answer
