from collections import deque
def solution(A, B):
    answer = 0
    Asortq = deque(sorted(A, reverse=True))
    Bsort = sorted(B, reverse=True)
    while Asortq:
        if Asortq[-1] < Bsort[-1]:
            answer += 1
            Asortq.pop()
            Bsort.pop()
        else Asortq[-1] > Bsort[-1]:
            Asortq.popleft()
            Bsort.pop()
        
    return answer
