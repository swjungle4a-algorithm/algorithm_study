from collections import deque
def solution(A, B):
    answer = 0
    
    A.sort()
    B.sort()

    tmp_stk = []

    while A or B:
        if A[-1] < B[-1]:
            A.pop()
            B.pop()
            answer += 1
        else:
            A.pop()
            del B[0]

    return answer
