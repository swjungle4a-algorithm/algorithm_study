from heapq import heapify, heappop

def solution(A, B):
    answer = 0
    A.sort()
    heapify(B)
    for a in A :
        while B :
            b = heappop(B)
            if b > a :
                answer += 1
                break
    return answer
