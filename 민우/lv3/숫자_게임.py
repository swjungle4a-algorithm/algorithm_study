from heapq import heappop, heappush

def solution(A, B):
    answer = len(A)
    A.sort()
    B.sort()
    
    while B:
        a = heappop(A)
        b = heappop(B)

        if a >= b:
            heappush(A, a)
            continue
                    
    return answer - len(A)
