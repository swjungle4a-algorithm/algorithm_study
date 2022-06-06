from math import log2

def solution(n,a,b):
    M = int(log2(n))
    pivot = n // 2
    
    while True :
        if a <= pivot and b <= pivot :
            M -= 1
            pivot -= 2 ** (M-1)
            continue
        elif (a > pivot and b > pivot) :
            M -= 1
            pivot += 2 ** (M-1)
            continue
        return M
