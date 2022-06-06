def solution(A, B):
    A.sort(reverse = True)
    B.sort(reverse = True)
    idx = 0
    for a in A:
        if a < B[idx]: idx += 1
        if idx == len(A): break
    return idx
