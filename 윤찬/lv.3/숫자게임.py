def solution(A, B):
    answer = 0
    A = sorted(A)
    B = sorted(B)
    for a in A:
        idx = 0
        for b in B:
            if a < b:
                answer += 1
                del B[idx]
                break
            idx += 1        
    return answer
