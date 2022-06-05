from math import ceil

def solution(n,a,b):
    answer = 0
    
    while a != b :
        answer += 1
        a = ceil(a/2)
        b = ceil(b/2)

    return answer
