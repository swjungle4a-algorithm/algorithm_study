def solution(cookie):
    answer = 0
    N = len(cookie)
    for i in range(N):
        set1 = set()
        set2 = set()
        tmp = 0
        for j in range(i, -1, -1):
            tmp += cookie[j]
            set1.add(tmp)
        tmp = 0
        for k in range(i+1, N):
            tmp += cookie[k]
            set2.add(tmp)
        set3 = set1 & set2
        if set3:
            answer = max(answer, max(set3))
    return answer
